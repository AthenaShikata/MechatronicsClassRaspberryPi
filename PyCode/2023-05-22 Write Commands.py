import requests
url_path = 'https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/' 
url_file = 'all_robots_command_requests.txt'
url = url_path + url_file
r = requests.get(url)
whole_file = r.text
xFile = open('commands.txt','w')
xFile.write(whole_file)