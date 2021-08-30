class info:
    "personal information"
    def __init__(self):
        self.info=""
    def information(self):
        self.info=input("input the information")
    def setdata(self):
        print("ino:",self.info)
x=info()
x.information()
x.setdata()
        
