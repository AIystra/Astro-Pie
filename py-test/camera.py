from picamzero import Camera
from time import sleep
#importe la librairie nécessaire au controle de la caméra et
#sleep qui permet d'attendre pour espacer les photos

#on peut prndre 42 photos donc on va les prendre en 7 min donc 6/min une tt les 10s
camera=Camera()
for i in range(42): #on prend nos 42 photos
    camera.take_photo("image_{:02d}.jpg".format(i+1)) #prend une photo avec pour format image
    sleep(10) #attends 10S

