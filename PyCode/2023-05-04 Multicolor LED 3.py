import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

R = 7
G = 5
B = 3
PINS = [R,G,B]
GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(R,1)
GPIO.output(G,1)
GPIO.output(B,1)
try:
    while True:
        request = input("Enter RGB Hex: ")
except KeyboardInterrupt:
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)


('''
        if len(request) == 3:
            GPIO.output(R,int(request[0]))
            GPIO.output(G,int(request[1]))
            GPIO.output(B,int(request[2]))
            ''')