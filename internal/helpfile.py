from .helplist import *
def helper():
    print('Available commands:')
    print(helpdata)
    print("Run command describe [COMMAND] for description of certain command.")
if __name__=="__main__":
    helper()