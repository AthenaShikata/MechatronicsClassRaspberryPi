import webbrowser
import sys
try:
    if len(sys.argv) > 1 :
        # get argument string from command line
        cmd_parameter = ''.join(sys.argv[1:])
    print(cmd_parameter)
    if len(sys.argv) > 1 :
        # get argument string from command line
        cmd_parameter2 = ''.join(sys.argv[1])
    print(cmd_parameter2)
    if len(sys.argv) >=2 :
        # get argument string from command line
        cmd_parameter3 = ''.join(sys.argv[2])
    print(cmd_parameter3)
except:
    print('no cmd parameter provided') 