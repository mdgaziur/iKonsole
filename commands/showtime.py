import time, datetime
from datetime import *


def showtime(tokens):
    try:
        t = tokens[1]
        if t == 'custom':
            t1 = tokens[2]
        if t == 'default':
            time = datetime.now()
            print(time.strftime("Current time: %I:%M:%S %p %Z\nDate: %d %B, %Y"))
        elif t == 'custom':
            try:
                time = datetime.now()
                formattime = ''
                for x in tokens[2:]:
                    formattime = formattime + x
                print(time.strftime(formattime))
            except:
                print("Invalid format.")
        else:
            print("Invalid option.")
    except:
        print(
            "Too few arguments given.\nThe format of giving arguments: 'showtime [OPTION] [FORMAT].\n2 options are available.")
        print(
            "One is 'default' another is 'custom. In case of 'default' option, the program will show time according to its default format. [FORMAT] argument is unneccessary this time.")
        print(
            "In case of 'custom' option, it is required to give the format of showing time.")
