from gpiozero import Button, Servo
from signal import pause
import cv2
from picamera import PiCamera
from datetime import datetime
import time
import telebot
from time import sleep
import subprocess
##import pygame, sys
##import pygame.camera

TOKEN='766936446:AAEqBsUsCwl6M76-fDKJQveJ72fPkfPaFi8'
bot = telebot.TeleBot(TOKEN)
#global time
tiempo = datetime.now()
servoPort = 17
servo = Servo(servoPort)
#cam = cv2.VideoCapture(0)
servo.min()
disponible = True

##camera=PiCamera()

def geordie_gay():
    print('OPRIMIDO')
    global tiempo
    global disponible
##    pygame.init()
##    pygame.camera.init()
##    cam = pygame.camera.Camera('dev/video0', (width, height))
##    cam.start()
##    image = cam.get_image()
##    cam.stop()
##    pygame.image.save(image, 'picture.jpg')
    # initialize the camera
    tie = datetime.now()
    diferencia = tie-tiempo
    print(diferencia.seconds)
    tiempo = tie
    servo.max()
    sleep(1)
    servo.min()
    sleep(1)
    disponible = True
    if(diferencia.seconds > 0): #cambiar a 15
        try:
            print(bot.get_me())
            #cam = cv2.VideoCapture(0)
            #ret, image = cam.read()
            
            #cam.release()
    ##    camera.capture('/home/pi/Desktop/%s.jpg' % tie)
            #if(ret):
                #cv2.waitKey(1)
                #cv2.imwrite('/home/pi/Desktop/'+tie.isoformat()+'.jpg',image)
                #print("IMAGEN GUARDADA")
            #cam.release()
            #time.sleep(0.2)

            programa = subprocess.call("fswebcam " +tie.isoformat()+".jpg", shell = True)
            print("IMAGEN TOMADA")
            time.sleep(0.5)
            if(programa == 0):
                print("IMAGEN TOMADA")
            else:
                print("IMAGEN no TOMADA")
            
            photo = open('/home/pi/Desktop/'+tie.isoformat()+'.jpg','rb')
            #photo = open('/home/pi/Desktop/
            print('Imagen abierta')
            time.sleep(0.3)
            print('Enviando imagen')
            bot.send_photo(585165361,photo)
            print('Imagen Enviada')
            #subprocess.call("pkill fswebcam")
            #cam.release()
        except:
            print('ERROR FOTO')
##

button = Button(15)

button.when_pressed = geordie_gay

pause()
