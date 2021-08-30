class Car:
       print("Wel Come to Showroom")
       def __init__(self):
              self.name="Fierd"
              self.color="Red"
       def show1(self):
              print("Car Name: ", self.name)
              print("Car Color: ", self.color)
                         
class Maruti(Car):
       print ("Maruti")
       def detail(self):
              Car.__init__(self)
              self.speed="180/hrs"
              self.category="Normal Van"
              
       def show1(self):
              print("Car Name: ", self.speed)
              print("Car Color: ", self.category)

              
class Swift(Car):
       def detail(self):
              Car.__init__(self)
              self.speed="280/hrs"
              self.category="Luczxry Car"
       def show1(self):
              print("Car Name: ", self.speed)
              print("Car Color: ", self.category)


a=Maruti()
a.detail()
a.show1()
#print ("Swift")
#c=Swift()
#c.detail()
#c.show1()






