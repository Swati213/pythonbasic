class Personal_info :
    def __init__ (self):
        self.name = None
        self.age = None
        self.mobile = None
        self.address = None


    def show_info(self):
        print "Name {0}, Age {1}, Mobile {2}, Address {3}".format (self.name, self.age, self.mobile,self.address)

class Student_info(Personal_info):
    def __init__(self):
        Personal_info . __init__(self)



p = Student_info()
p.show_info ()


        

    
        
