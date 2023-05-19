import requests

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

robot_names = {}
robot_commands = []
flag_colors=('#000000','#a5a6a5','#ffffff','#820082',)

def send_commands(i,flag_current):
    robot_line={'robotName':'ace_bot','robotDevice':'rgb-led','robotInstruction':flag_colors[flag_current]}
    send_url = 'https://www.steamclown.org/projects/QInlIj_vIHev/QInlIj_vIHev.php'
    x = requests.post(send_url, data = robot_line)
    print('ace_bot',flag_colors[flag_current])
    print(x.text)

def main():
    flag_current = 0
    for i in range(20):
        send_commands(i,flag_current)
        print('')
        flag_current = flag_current+1
        if flag_current == 4:
            flag_current = 0
    
main()