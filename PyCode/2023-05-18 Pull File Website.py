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

def url_ok(url):
    try:
        response = requests.head(url)
    except Exception as e:
        return "NOT OK: Website Not Found"
    else:
        if response.status_code == 200:
            return "OK: Website Found"
        else:
            return "NOT OK: Other Error"

def get_name(i):
    x = requests.get(urls[i])
    text = x.text
    #print(text)
    foundRobotStart = text.find('robot_name = ')
    if foundRobotStart == -1:
        print('ERROR: No Bot Found')
    else:
        foundStart = foundRobotStart + 13
        foundEnd = text.find('<',foundStart)
        #print(foundRobotStart)
        #print(foundStart)
        #print(foundEnd)
        #print(text[foundRobotStart],text[foundStart],text[foundEnd])
        found_robot_name = text[foundStart:foundEnd].strip()
        print(found_robot_name)

def test(i):
    print(i)
    url_check = url_ok(urls[i])
    print(url_check)
    if url_check == 'OK':
        try:
            x = requests.get(urls[i])
        except:
            raise TyperError('URL Not Able To Connect')
        text = x.text
        print(text)
        foundRobotStart = text.find('robot_name = ')
        foundStart = foundRobotStart + 13
        foundEnd = text.find('<',foundStart)
        print(foundRobotStart)
        print(foundStart)
        print(foundEnd)
        print(text[foundRobotStart],text[foundStart],text[foundEnd])
        found_robot_name = text[foundStart:foundEnd].strip()
        print(found_robot_name)

def main():
    #test('Brian N')
    for i in urls:
        print(i,urls[i])
        url_check = url_ok(urls[i])
        print(url_check)
        if url_check == 'OK':
            get_name(i)
        print('')



main()


('''url = "http://10.178.203.129/"
x = requests.get(url)
whole_file = x.text
print(whole_file)
whole_file = whole_file.content()
print(whole_file)
''')


('''url = 'https://www.steamclown.org/projects/QInlIj_vIHev/QInlIj_vIHev.php'
robot_line={'robotName':'robot2','robotDevice':'rgb-led','robotInstruction':'red'} 
xFile = open('scrape.txt','w')

x = requests.post(url, data = robot_line)

#print the response text (the content of the requested file):
print(robot_line)
print(x.text) # message retured from the request.post()''')


('''Scrape someones file name send it to burnhams website
read your commands from burnhams website, run your commands''')