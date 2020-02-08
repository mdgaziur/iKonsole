import shutil
import os


def startmoving(tokens):
    if os.path.isfile(tokens[1]):
        if os.path.isdir(tokens[2]):
            print("Moving...")
            shutil.move(tokens[1], tokens[2])
            print("Successfully moved!")
        else:
            print("No such directory called: %s!" % tokens[2])
    else:
        print("No such file called: %s!" % (tokens[1]))


def move(tokens):
    if len(tokens) < 2 or len(tokens) < 3:
        print("Not enough arguments given.")
    else:
        startmoving(tokens)
