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
        R, G, B = list(request[i:i+2] for i in 6)
        print(R+G+B)
        ('''if len(request) == 6:
            R, G, B = tuple(hex(request[i:i+2], 16) for i in (0, 2, 4))
            print(R+G+B)''')
except KeyboardInterrupt:
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)
