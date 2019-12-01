# Still developing...
from .exceptions import *


def parse(file=None):
    preprocessed=[]
    if file is None:
        ParseError("4")
    else:
        f=open(file,"r")
    count=0
    while True:
        data=f.readline()
        data=data.split()
        if count==0:
            if data[0]=="command_group{":
                preprocessed.append("import time")
                preprocessed.append("subprocess")
            else:
                ParseError("1")
        else:
            if data[0]=="wait":
                try:
                    t=data[1]
                    preprocessed.append("SLEEP "+t+"\n")
                except:
                        ParseError("1")
            elif data[0]=="process":
                try:
                    cmd=data[1:]
                    preprocessed.append("RUN ")
                except:
                    ParseError("1")
            elif data[0]=="}done":
                break
            else:
                ParseError("1")
            f.close()
            new=open("temp.py","w+")
            new.write(' '.join(preprocessed))
            new.close()
            with open("temp.py","r") as rnf:
                exec(rnf.read())


