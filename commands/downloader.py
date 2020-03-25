import requests
import sys
import time
import shutil

chunk_size = 1024

def autoconvert(length):
    length=float(length)
    s=round(length/1048576,2)
    if s<1024:
        return str(s)+" MB"
    elif s>=1024:
        return str(round(s/1024,2))+" GB"
    elif s>=1024*1024:
        return str(round(s/(1024*1024),2))+" TB"
    

def Download():
    console_columns,console_rows=shutil.get_terminal_size()
    scls=(25*console_columns)//120
    url=input("Enter the url for downloading file: ")
    filename=url.split('/')[-1]
    if "?" in filename:
        filename=filename.split('?')
        filename=filename[0]
    try:
        response=requests.get(url,stream=True)
    except ConnectionError:
        print("Cannot connect to the destination url!")
        return 1
    except ConnectionAbortedError:
        print("The server actively refused to connect!")
        return 1
    except:
        print("Cannot connect to the server!")
        return 1
    dest=input("Enter the destination(with \ at the end): ")
    file_length=response.headers['content-length']
    curdown=0
    try:
        with open(dest+filename,"wb") as f:
            if file_length==0:
                f.write(response.content)
            else:
                for data in response.iter_content(chunk_size=chunk_size):
                    console_columns,console_rows=shutil.get_terminal_size()
                    scls=(25*console_columns)//120
                    curdown+=len(data)
                    percent=(curdown*50)/(float(file_length))
                    f.write(data)
                    barcount=int((percent*scls)//50)
                    spacecount=scls-barcount
                    ac=autoconvert(curdown)
                    af=autoconvert(file_length)
                    print("\rDownloading",filename,"[","█"*barcount," "*spacecount+"]",ac,"/",af,round((100*percent)/50,2),"%",file=sys.stdout,end='')
                    sys.stdout.flush()
    except PermissionError:
        print("Cannot create file in %s! Do you have the permission to do this?"%(dest))
    print()
    print("Download Completed!")
def downloader(temp):
    Download()