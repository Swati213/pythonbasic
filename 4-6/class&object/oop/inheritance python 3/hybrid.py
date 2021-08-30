#hybrid inheritance
class Bike :
       def __init__ (self):
              self.name = "Pulsar"
              self.color = "Blue"
       def b_show (self):
              print ("Name : ",self.name)
              print ("Color : ",self.color)
class Range:
       def __init__(self):
              self.speed = "80km/h"
       def r_show(self):
              print ("Speed : ",self.speed)
class Model(Bike,Range) :
       def __init__(self):
              Bike.__init__(self)
              Range.__init__(self)
              self.model = "t20"
       def m_show (self):
              Bike.b_show(self)
              Range.r_show(self)
              print ("Model : ",self.model)
class Engine(Model):
       def __init__(self):
              Model.__init__(self)
              self.engine = "Pata N kaisa hota hai...hahahah"
       def e_show(self):
              Model.m_show(self)
              print("Engine : ",self.engine)
                     
#b = Bike()
#b.b_show()
#r = Range()
#r.r_show()
#m = Model()
#m.m_show()
e = Engine()
e.e_show()






              
       
