import webbrowser
import sys
try:
    if len(sys.argv) > 1 :
        # get argument string from command line
        cmd_parameter = ''.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + cmd_parameter)
except:
    print('no address provided') 
