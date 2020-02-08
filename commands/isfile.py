import os


def isfile(tokens):
    try:
        exists = os.path.isfile(tokens[1])
        if exists:
            print('File "' + tokens[1] + '" exists.')
        elif not exists:
            print('File "' + tokens[1] + '" does not exists.')
    except:
        print("No file given for checking it's existance.")
