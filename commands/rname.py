import os


def rname(tokens):
    try:
        temp = tokens[1]
        temp1 = tokens[2]
        if os.path.exists(tokens[1]):
            os.rename(tokens[1], tokens[2])
        else:
            print("No such file or directory named: '" + tokens[1] + "'!")
    except:
        print("Too few arguments are given.\nThe format of giving arguments: 'rname [FILENAME] [NEWNAME]'.")
