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
            try:
                red = int(request[0:2],16)
                green = int(request[2:4],16)
                blue = int(request[4:6],16)
                print(red,green,blue)
                GPIO.output(R,red)
                GPIO.output(G,green)
                GPIO.output(B,blue)
            except:
                raise TypeError('Value Not Hexadecimal')
except KeyboardInterrupt:
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)
    pass
