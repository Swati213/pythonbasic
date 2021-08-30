#multilevel Inheritance
class Car :
    def Details (self):
        self.name = "Fierd"
        self.color = "White"
        print "Car Name : ",self.name, "Car Color :",self.color

class Maruti (Car) :
    def Features (self):
        self.speed = "180/hrs "
        self.category = "Normal Van"
        print "Maruti Speed : ",self.speed ,"Maruti Category :" ,self.category
class Swift (Maruti) :
    def Features (self):
        self.speed = "280/hrs "
        self.category = "Luczxry Car"
        print "Swift Speed : ",self.speed ,"Swift Category :" ,self.category        

s = Swift()
s.Features()
q = Maruti ()
q.Features()

