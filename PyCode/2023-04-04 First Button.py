#
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Note:physical pins 
#GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(40,GPIO.IN)


led = 5
buttonPin = 40
toggle = 0
button = 0
press = 1
count = 0

while(True):
    press = GPIO.input(buttonPin)
    GPIO.output(led,press)
    if (press == 1):
        button = 0
    elif (press == 0):
        if (button == 0):
            button = 1
            if (toggle == 0):
                toggle = 1
                count += 1
            elif (toggle == 1):
                toggle = 0
                print(count)
                
                
    
    ('''state = GPIO.input(40)
    print(state)
    GPIO.output(led,state)
    ''')