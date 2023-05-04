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
        request = input("Enter RGB Hex (ex '#FF00A7' or 'FF00A7'): ")
        request = request.strip('\n#')
        if len(request) == 6:
            red = hex(request[0,1])
            green = hex(request[2,3])
            blue = hex(request[4,5])
            print(red+green+blue)
except KeyboardInterrupt:
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)
