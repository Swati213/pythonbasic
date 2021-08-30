""" aggregation with out using """
class Driver:
       def __init__(self):
              self.name="Ramu"
              self.age = "30"
              self.name2="Jhon"
              self.age2 = "25"
       def d1_show(self):
              a="Driver = 1"
              print (a.center(20,"*"))
              print ("Name = ",self.name)
              print("Age = ",self.age)
       
       def d2_show(self):
              a="Driver = 2"
              print (a.center(20,"*"))
              print ("Name = ",self.name2)
              print("Age = ",self.age2)

class Car:
       def __init__(self):
              self.name="Hyundai"
              self.model = "i20"
              self.name2="Ford"
              self.model2 = "figo"
              
       def c1_show(self):
              a="Car = 1"
              print (a.center(20,"*"))
              print ("Name = ",self.name)
              print("Model = ",self.model)
              
       
       def c2_show(self):
              a="Car = 2"
              print (a.center(20,"*"))
              print ("Name = ",self.name2)
              print("Age = ",self.model2)
      
#d = Driver()
#d.d1_show()
#d.d2_show()

c = Car()
c.c1_show()
c.c2_show()



