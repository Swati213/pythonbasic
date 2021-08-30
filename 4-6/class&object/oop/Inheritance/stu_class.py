class Pinfo:
    def __init__(self, name, email, mobile, addrs):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.addrs = addrs

class Student(Pinfo):
    def __init__(self, name, email, mobile, addrs):
        Pinfo.__init__(self, name, email, mobile, addrs)
        self.reg_no = None
        self.stuclass = None
        self.marks = {"H":0, "E":0, "M":0, "S":0, "C":0}

obj = Student("Prakash","prakash@mail.com","8808527577","Allahabad")
print obj.reg_no
print obj.marks
print obj.stuclass
print obj.name
print obj.email
print obj.mobile
print obj.addrs
        
