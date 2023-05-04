import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

redPin = 7
greenPin = 5
bluePin = 3

while(True):
    GPIO.output(redPin,1)
    GPIO.output(greenPin,1)
    GPIO.output(bluePin,1)