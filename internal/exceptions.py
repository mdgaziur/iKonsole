class ParseError():
    def __init__(self,errcode,message=None):
        self.errcode=errcode
        if not message is None:
            print(message)
        else:
            self.check_errcode()
    def check_errcode(self):
        code=self.errcode
        if code=="1":
            error="Invalid Syntax!"
        elif code=="2":
            error="Command not specified!"
        elif code=="3":
            error="No data in file!"
        elif code=="4":
            error="No file specified"
        self.print_error(error)
    def print_error(self,error):
        self.message="Errors occured while parsing command group file![Errno %d]: "%(int(self.errcode))+error
        self.__init__()