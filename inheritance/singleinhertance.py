"""single inheriteriance using super()"""
class personal:
    def __init__(self,fname,sname):
        self.fname=fname
        self.sname=sname
    def printname(self):
        print(self.fname,self.sname)
class student(personal):
    def __init__(self,fname,sname):
        super().__init__(fname,sname)#personal.__init__(self,fname,sname)
    def show(self):
        personal.printname(self)
        print("feature 1 is working")
obj=personal("Ramia","khanna")
obj.printname()
x=student("kabir","singh")
x.show()

































































































































































































































































       























































































































































































































































































































































































































































































 
