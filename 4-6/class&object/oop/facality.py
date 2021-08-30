class facality:
    print "spectrum"
    print "123"
    def __init__(self):
        self.name = "Arjun"
        self.age = "2e"
        self.mobile = 947474674
        self.address = raw_input("enter the number")
        #self.email = raw_input("enter the number")
    def show(self):
        print self.name
        print self.age
        print self.mobile
        print self.address
        #print self.email

f = facality()
f.show()
