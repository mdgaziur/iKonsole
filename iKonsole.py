# verify python verision
from verify_pyver import verify

verify()
#importng os and system
import os,sys
#importing subprocess module
import subprocess
#importing getpass module
import getpass
#importing shlex module
import shlex
if sys.platform!="win32":
    try:
        import readline
    except:
        try:
            import gnureadline
        except:
            print("Neither 'readline' nor 'gnureadline' module not found. Readline capabilities will not be available.")
from datetime import datetime
#importing required modules from internal folder
from internal.config import *
from internal.helpfile import helper
from internal.descriptor import *
from cexec import cexec
from commands_list import *

for cmd in IKONSOLE_CMD_BUILTIN:
    exec('from commands.' + cmd + ' import ' + cmd)
mhome=os.path.dirname(__file__)
dir=os.getcwd()
username=getpass.getuser()
print('iKonsole v'+iversion+'. Python '+pyver+'. Running on '+OS+' '+os_release+'.')


def command_exists(command):
    if command in IKONSOLE_CMD_BUILTIN:
        return True
    return False
while(1):
    try:
        line=input(username+'@'+OS+'-\''+os.getcwd()+'\'>>>')
    except:
        sys.exit(1)
    tokens=line.split()
    none=False
    try:
        temp=tokens[0]
    except:
        none=True
    if none:
        pass
    elif tokens[0] == 'help':
        helper()
    elif tokens[0] == 'exit':
        sys.exit()
    elif tokens[0] == 'about':
        show_description()
    else:
        if command_exists(tokens[0]):
            cexec(tokens, IKONSOLE_CMD_BUILTIN)
        else:
            try:
                if sys.platform == "win32":
                    os.system(line)
                else:
                    output = subprocess.run(shlex.split(line), stdout=subprocess.PIPE)
            except:
                print("No such program or command called '" + line + "'")







'''

////            Tell me if you liked this project :)            ////
////    BE HAPPY AND DON'T HATE PROJECTS FROM BEGINNERS :)      ////


'''
