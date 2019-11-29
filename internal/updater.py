'''Updater for iKonsole.
Downloads a html file containing only the latest version number and checks with the current version.
If it is bigger than installed version, the updater will prompt the user weather to update or not.
After downloading the new update iKonsole will be turned of and all updates will be applied by running
the setup with flag "--update". Which will replace and reconfigure the files.'''
def checkupdate():

def update(version=0.0):
    if version="0.0":
        print("Invalid version!")
    else:
        checkupdate()