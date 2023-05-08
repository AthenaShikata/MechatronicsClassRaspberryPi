import requests
#first parameter of the 'get' method is the 'url':
url = 'https://w3schools.com/python/demopage.htm'
x = requests.get(url)
#print the response text (the content of the requested file):
print(x.text)