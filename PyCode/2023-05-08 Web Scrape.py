import requests
#first parameter of the 'get' method is the 'url':
url = requests.get('https://w3schools.com/python/demopage.htm')
#print the response text (the content of the requested file):
print(url.text)