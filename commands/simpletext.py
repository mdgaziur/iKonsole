'''
A builtin simple text file maker.
'''


def save(data):
    fnaddr = input("Enter the filename with location: ")
    try:
        with open(fnaddr, "w+") as fp:
            fp.write(data)
    except:
        pass


def simpletext(bogus_arg):
    print("Type text from the next file and type 'sAvE FiLe simpletext' to save file")
    data = ''
    count = 1
    while (1):
        line = input()
        if line == 'sAvE FiLe simpletext':
            save(data)
            return
        if count == 1:
            count += 1
            data += line
        else:
            data += '\n' + line
