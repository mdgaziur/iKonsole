import platform, sys


def verify():
    pyver = platform.python_version()
    if int(pyver[0]) < 3:
        print("Cannot run iKonsole on Python with version less than 3.0")
        sys.exit(1)
    else:
        pass
