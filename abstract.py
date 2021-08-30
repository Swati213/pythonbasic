from abc import ABC, abstractmethod
class Animal(ABC):
       def info (self):
              print ("Aniaml leave in forest")

class Human(ABC):
       def info (self):
              print ("Human leave in city")

class Snake(Animal):
       def info (self):
              Animal.info(self) #abstract base class
              print ("Snake is danger animal")

class C_human(Human):
       def info (self):
              Human.info(self)  #abstract base class         
              print ("CITY HUMAN")




d = Snake()
d.info()
h = C_human()
h.info()
       
