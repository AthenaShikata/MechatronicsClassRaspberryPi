import requests

#Enter a url to find the title of the web page
url = 'https://steamclown.org/'
try:
    x = requests.get(url)
except:
    raise TyperError('URL Not Able To Connect')
text = x.text

titleStart = 7 + int(text.find('<title>'))
titleEnd = text.find('</title>')

print(text[titleStart:titleEnd])