'''Updater for iKonsole.
Downloads a html file containing only the latest version number and checks with the current version.
If it is bigger than installed version, the updater will prompt the user weather to update or not.
After downloading the new update iKonsole will be turned off and all updates will be applied by running
the setup with flag "--update". Which will replace and reconfigure the files.'''
#
#
#An Unprofessional way to update software...
#
#
import requests
from .config import *
import subprocess
import shlex
def checkupdate():
    lv=requests.get("https://mdgaziur.github.io/updateikonsole/")
    lv=lv.text.replace("\n","")
    return float(lv)
def download_update():
    returncode=subprocess.run(shlex.split("git clone https://github.com/mdgaziur/iKonsole.git"),stdout=subprocess.PIPE)
    if returncode!=0:
        print("Failed to download update!")
    else:
        print("Successfully downloaded.")
        print("Running setup with argument '--update'...")
        returncode=subprocess.run(shlex.split("./ikonsole-setup.py --update"),stdout=subprocess.PIPE)
        if returncode:
            print("Failed to install!")
        else:
            print("Installation/update successful!")
            print("Restarting iKonsole...")

def update():
    if iversion==0.0:
        print("Invalid version!")
    else:
        latver=checkupdate()
        curver=float(iversion)
        if latver<=curver:
            print("New update is available! Latest version of this software is: %f"%(latver))
            download_update()
        elif latver==curver:
            print("No update available. Current version is the latest.")
        else:
            print("Invalid version number!\nTry reinstalling the software or contact the developer.")

    pass
def update(version=0.0):
    if version=="0.0":
        print("Invalid version!")
    else:
        checkupdate()