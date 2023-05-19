import requests
import sys
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

urls = {'Mr. Burnham':'http://10.178.200.149',
'Evan Peres':'http://10.178.203.129/',
'Joshua Valenzuela':'http://10.178.203.127',
'Nam Nguyen':'http://10.178.203.125/',
'Landon Phan':'http://10.178.203.140/',
'Arlette Lopez':'http://10.178.203.124',
'Nancy Malu Romero':'http://10.178.203.123',
"Da'Quan B.":'http://10.178.203.44',
'Thaison N.':'http://10.178.203.2',
'Aiden V':'http://10.178.202.58/',
'Jessica Y':'http://10.178.203.83/',
'Andy H':'http://10.178.202.166/',
'Loc P':'http://10.178.201.175/',
'Tyler H':'http://10.178.203.82/',
'Nguyen V':'http://10.178.202.105/',
'Hayden M':'http://10.178.203.117',
'Kenny':'http://10.178.202.65',
'Brian N':'http://10.178.203.128/'}

robot_names = {'http://10.178.203.129/':'ace_bot'}
robot_commands = []

flag_colors=('#000000','#a5a6a5','#ffffff','#820082',)

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

def url_ok(url):
    try:
        response = requests.head(url)
    except Exception as e:
        print("NOT OK: Website Not Found")
        return 'bad'
    else:
        if response.status_code == 200:
            print("OK: Website Found")
            return 'good'
        else:
            print("NOT OK: Other Error")
            return 'bad'

def get_name(i):
    x = requests.get(urls[i])
    text = x.text
    foundRobotStart = text.find('robot_name = ')
    if foundRobotStart == -1:
        print('ERROR: No Bot Found')
        return 'bad'
    else:
        foundStart = foundRobotStart + 13
        foundEnd = text.find('<',foundStart)
        found_robot_name = text[foundStart:foundEnd].strip('<>();\n[:] ')
        robot_names[urls[i]]=found_robot_name
        print(found_robot_name)
        return found_robot_name
    
def send_commands(i,flag_current):
    robot_line={'robotName':robot_names[urls[i]],'robotDevice':'rgb-led','robotInstruction':flag_colors[flag_current]}
    send_url = 'https://www.steamclown.org/projects/QInlIj_vIHev/QInlIj_vIHev.php'
    x = requests.post(send_url, data = robot_line)
    print(robot_names[urls[i]],flag_colors[flag_current])
    print(x.text)

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
    flag_current = 0
    for i in urls:
        print(i,urls[i])
        url_check = url_ok(urls[i])
        if url_check == 'good':
            found_name = get_name(i)
            if found_name != 'bad':
                send_commands(i,flag_current)
        print('')
        flag_current = flag_current+1
        if flag_current == 4:
            flag_current = 0
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