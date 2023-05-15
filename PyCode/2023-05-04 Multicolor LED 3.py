import sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

R = 32
G = 33
B = 35
PINS = [R,G,B]
GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
red_pwm = GPIO.PWM(R,1000)
green_pwm = GPIO.PWM(G,1000)
blue_pwm = GPIO.PWM(B,1000)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

try:
    while True:
        request = input("Enter RGB Hex Code (ex '#FF00A7' or 'FF00A7'): ")
        request = request.strip('\n#')
        if len(request) == 6:
            try:
                red = int(request[0:2],16) * (100/255)
                green = int(request[2:4],16) * (100/255)
                blue = int(request[4:6],16) * (100/255)
                print(red,green,blue)
                red_pwm.ChangeDutyCycle(red)
                green_pwm.ChangeDutyCycle(green)
                blue_pwm.ChangeDutyCycle(blue)
            except:
                print('Value Not Hexadecimal. Please Enter A Hexadecimal Color Code')
        else :
            print('Value Not Hexadecimal. Please Enter A Hexadecimal Color Code')
except KeyboardInterrupt:
    print('Closing Program')
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)