import requests
import sys
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

robot_commands = []

def get_commands():
    url_path = 'https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/' 
    url_file = 'all_robots_command_requests.txt'
    url = url_path + url_file
    r = requests.get(url)
    whole_file = r.text
    foundStart = whole_file.find('ace_bot')
    while foundStart != -1:
        foundEnd = whole_file.find('\n',foundStart)
        print(foundStart)
        print(foundEnd)
        command = whole_file[foundStart:foundEnd]
        command = command.strip()
        print(command)
        robot_commands.append(command)
        foundStart = whole_file.find('ace_bot',foundEnd)
        print('')

def run_command(request):
    try:
        request = request.strip('\n#')
        if request == 'red':
            red_pwm.ChangeDutyCycle(255)
            green_pwm.ChangeDutyCycle(0)
            blue_pwm.ChangeDutyCycle(0)
            print('red')
        elif request == 'green':
            red_pwm.ChangeDutyCycle(0)
            green_pwm.ChangeDutyCycle(255)
            blue_pwm.ChangeDutyCycle(0)
            print('green')
        elif request == 'blue':
            red_pwm.ChangeDutyCycle(0)
            green_pwm.ChangeDutyCycle(0)
            blue_pwm.ChangeDutyCycle(255)
            print('blue')
        elif len(request) == 6:
            try:
                red = int(request[0:2],16) * (100/255)
                green = int(request[2:4],16) * (100/255)
                blue = int(request[4:6],16) * (100/255)
                print(red,green,blue)
                red_pwm.ChangeDutyCycle(red)
                green_pwm.ChangeDutyCycle(green)
                blue_pwm.ChangeDutyCycle(blue)
            except:
                print('Value Not Hexadecimal or Red, Green, or Blue. Please Enter A Valid Color')
        else :
            print('Value Not Hexadecimal or Red, Green, or Blue. Please Enter A Valid Color')
    except KeyboardInterrupt:
        print('Closing Program')
        red_pwm.stop()
        green_pwm.stop()
        blue_pwm.stop()
        GPIO.output(R,0)
        GPIO.output(G,0)
        GPIO.output(B,0)

def main():
    get_commands()
    print(robot_commands)
    print('')
    for i in robot_commands:
        i = i.split(',')
        color = i[2]
        print(color)
        run_command(color)
        time.sleep(2)
        print('')
    print('Closing Program')
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.output(R,0)
    GPIO.output(G,0)
    GPIO.output(B,0)

main()