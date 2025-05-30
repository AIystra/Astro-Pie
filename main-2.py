from picamzero import Camera
from time import sleep, time
from exif import Image
from datetime import datetime
import cv2
import math

# Major Improvement :
# No improvement : 7.2km/s
# Wirte time : 7.4km/s : Improves accuracy by 2.77%
# Curvature of the earth : 7.7km/s : Improves accuracy by 4.05%
# Taking into account clouds is essential to calculate speed, because the Earth essentially consists of 70% ocean at the surface, clouds are essential if not land.

# Function to extract the time an image was taken from metadata
def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time

# Calculate the writing time of an image
def writing(image):
    start = time()
    cv2.imwrite("temp_image.jpg", image)
    end = time()
    return(end - start)

# Get the time difference between two images taking into account their writing times
def get_time_difference(image_1, image_2, write_time):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_difference = (time_2 - time_1).total_seconds() - write_time
    return time_difference

# Converts images to OpenCV (grayscale) format
def convert_to_cv(image_1, image_2):
    return cv2.imread(image_1, 0), cv2.imread(image_2, 0)

# Get width of an image
def get_width(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        width = img.get("pixel_x_dimension")
        return width

# Calculate the gsd
def compute_gsd(image_width):
    altitude = 420000 # we suppose the iss altitude will be 420km
    focal = 7.689 # Deduced from historical data with https://wheretheiss.at/
    sensor_width = 6.287 # see https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/  
    return (100.0 * 6.287 * altitude) / (focal * image_width)

# Detection of characteristic points of images with ORB (Oriented FAST and Rotated BRIEF)
def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures=feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2, None)
    return keypoints_1, keypoints_2, descriptors_1, descriptors_2

# Compare image descriptors to find matches
def calculate_matches(descriptors_1, descriptors_2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2)
    return sorted(matches, key=lambda x: x.distance)

# Retrieves the coordinates of the corresponding points in the two images
def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    coordinates_1, coordinates_2 = [], []
    for match in matches:
        coordinates_1.append(keypoints_1[match.queryIdx].pt)
        coordinates_2.append(keypoints_2[match.trainIdx].pt)
    return coordinates_1, coordinates_2

# Calculate the average of the distances between each featurs of one image and another, while taking into account their distance from the center of the image (curvature of the earth which can have an influence on the real distance)
def calculate_corrected_distance(coordinates_1, coordinates_2, image_size): 
    center_x, center_y = image_size[1] / 2, image_size[0] / 2 # Image center
    all_distances = 0
    for (x1, y1), (x2, y2) in zip(coordinates_1, coordinates_2):
        base_distance = math.hypot(x1 - x2, y1 - y2) # Euclidean distance between points
        distance_from_center = math.hypot(x1 - center_x, y1 - center_y) # Distance from point to center
        correction_factor = 1 + (distance_from_center / max(center_x, center_y)) * 0.1 # Correction factor
        all_distances += base_distance * correction_factor
    return all_distances / len(coordinates_1)

# Calculate speed in km/s
def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    if time_difference == 0:
        raise ValueError("The times elapsed between the two images are zero, impossible to calculate the speed.") # in case
    return (feature_distance * GSD / 100000) / time_difference

# Main function to calculate the speed of the ISS
def instruction(image_1, image_2):
    image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) # Create OpenCV image objects
    wtime1, wtime2 = writing(image_1_cv),writing(image_2_cv) # Calculate the time of writing an image
    time_difference = get_time_difference(image_1, image_2,wtime1 + wtime2) # Get time difference between images
    keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 10000) # Get keypoints and descriptors
    matches = calculate_matches(descriptors_1, descriptors_2) # Match descriptors
    coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches) # Extraction of coordinates
    corrected_distance = calculate_corrected_distance(coordinates_1, coordinates_2, image_1_cv.shape) # Correction of distances
    image_resolution = get_width(image_1)
    height, width = image_1_cv.shape
    gsd = compute_gsd(width)
    return calculate_speed_in_kmps(corrected_distance, gsd, time_difference) # Speed ​​calculation

liste_vitesse = []
camera = Camera()
for i in range(42):
    camera.take_photo(f"image_{i+1:02d}.jpg")
    if i != 0:
        liste_vitesse.append(instruction(f"image_{i:02d}.jpg", f"image_{i+1:02d}.jpg"))
    sleep(9)

vitesse_iss = sum(liste_vitesse) / len(liste_vitesse)
# Transforms the float into str and leaves 4 digits after the decimal point

with open("result.txt", "w") as fichier: # create a txt file to be able to modify it
    fichier.write(f"{vitesse_iss:.4f}") # put the speed in this file
