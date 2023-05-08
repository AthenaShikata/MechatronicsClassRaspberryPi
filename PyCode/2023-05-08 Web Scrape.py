import requests
#first parameter of the 'get' method is the 'url':
url = 'https://www.steamclown.org/projects/red_pill.html'
# url = 'https://www.steamclown.org/projects/red_pill.txt'
x = requests.get(url)
#print the response text (the content of the requested file):
print(x.text)