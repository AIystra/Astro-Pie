from orbit import ISS
from skyfield.api import load
t = load.timescale().now() # Obtain the current time `t` 
position = ISS.at(t) # Compute where the ISS is at time `t` 
location =position.subpoint() # Compute the coordinates of the Earth location directly beneath the ISS
altitude=location.elevation.km
longitude=location.longitude
latitude=location.latitude

