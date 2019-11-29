#importng os and system
import os,sys
#importing subprocess module
import subprocess
#import logger
import logging
#importing getpass module
import getpass
#importing shlex module
import shlex
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
#set timestamp in logfile
try:
    lf=open(mhome+'/debug.log','a')
    lf.write('======================================Debug log======================================\n')
    lf.close()
except:
    pass
#configuring logger
logging.basicConfig(filename='debug.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

dir=os.getcwd()
username=getpass.getuser()
print('iKonsole v'+version+'. Python '+pyver+'. Running on '+OS+' '+os_release+'.')
while(1):
    logging.info('Waiting for user input...')
    try:
        line=input(username+'@'+OS+'-\''+os.getcwd()+'\'>>>')
    except:
        logging.info('Exit signal triggered. Now terminating the application.')
        sys.exit(1)
    logging.info('Received user input')
    logging.info('Tokenizing input...')
    tokens=line.split()
    logging.info('Checking Input...')
    logging.info('Given command is "'+line+'". Now processing it.')
    none=False
    try:
        temp=tokens[0]
    except:
        none=True
    if none:
        pass
    elif tokens[0]=='cd':
        try:
            logging.info('Checking if it has no arguments...')
            white=False
            try:
                temp=tokens[1]
            except:
                logging.info('No argument is given. Now setting current directory to HOME')
                white=True
                if white:
                    if OS=="Windows":
                        os.chdir("C:\\User\\"+username)
                    else:
                        os.chdir("/home/"+username)
            else:
                logging.info('Path given. Now changing current directory to it.')
                os.chdir(tokens[1])
        except FileNotFoundError as e:
            logging.error('Directory "'+tokens[1]+'" does not exists!')
            print(e)
        except PermissionError as e:
            logging.error('No permission available to access directory "'+tokens[1]+'"')
            print(e)
    elif tokens[0]=='help':
        helper()
    elif tokens[0]=='repair-ikonsole':
        print('"Under construction" command.')
    elif tokens[0]=='exit':
        logging.info("Terminating iKonsole with exit code 0.")
        sys.exit(0)
    elif tokens[0]=="isfile":
        try:
            exists=os.path.isfile(tokens[1])
            if exists:
                print('File "'+tokens[1]+'" exists.')
            elif not exists:
                print('File "'+tokens[1]+'" does not exists.')
        except:
            print("No file given for checking it's existance.")
    elif tokens[0]=="rname":
        logging.info("Processing code for command 'rname'...")
        try:
            logging.info("Check if all the required arguments are present...")
            temp=tokens[1]
            temp1=tokens[2]
            logging.info("Changing the name of given file: '"+tokens[1]+"'...")
            if os.path.exists(tokens[1]):
                os.rename(tokens[1],tokens[2])
            else:
                print("No such file or directory named: '"+tokens[1]+"'!")
        except:
            logging.error("One or both of the required arguments are not present. Work stopped.")
            print("Too few arguments are given.\nThe format of giving arguments: 'rname [FILENAME] [NEWNAME]'.")
    elif tokens[0]=='showtime':
        try:
            logging.info("Check if all the required arguments are present...")
            t=tokens[1]
            if t=='custom':
                t1=tokens[2]
            if t=='default':
                time=datetime.now()
                print(time.strftime("Current time: %I:%M:%S %p %Z\nDate: %d %B, %Y"))
            elif t=='custom':
                try:
                    time=datetime.now()
                    formattime=''
                    for x in tokens[2:]:
                        formattime=formattime+x
                    print(time.strftime(formattime))
                except:
                    print("Invalid format.")
            else:
                print("Invalid option.")
        except:
            logging.error("One or both of the required arguments are not present. Work stopped.")
            print("Too few arguments given.\nThe format of giving arguments: 'showtime [OPTION] [FORMAT].\n2 options are available.")
            print("One is 'default' another is 'custom. In case of 'default' option, the program will show time according to its default format. [FORMAT] argument is unneccessary this time.")
            print("In case of 'custom' option, it required to give the format of showing time. Custom format should be given with ''.")
    elif tokens[0]=='about':
        show_description()
    elif tokens[0]=='remove_logfile':
        try:
            os.remove(mhome+'/debug.log')
            print('Debug file removed!\nRestart iKonsole for creating clean logfile')
        except:
            pass
    else:
        try:
            if sys.platform=="win32":
                os.system(line)
            else:
                output=subprocess.run(shlex.split(line),stdout=subprocess.PIPE)
        except:
            logging.error('No command found called: "'+line+'"')
            print("No such program or command called '"+line+"'")