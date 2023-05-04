import time, sys

request = 'FF00A7'
request = request.strip('\n#')
request = hex(int(request,16))
print(request)
print(type(request))

R=request[0,2]
G=request[2,4]
B=request[4,6]
print(R,G,B)