from abc import ABC, abstractmethod
class Animal(ABC):
       @abstractmethod
       def info (self):
              print ("Aniaml leave in forest")

class Human(ABC):
       def info (self):
              print ("Human leave in city")

class Snake(Animal):
       def info (self):
              super().info()
              print ("Snake is danger animal")
class V_human(Human):
       def info(self):
              super().info()
              print ("Village is beautiful")

class Dog(Animal):
       def info (self):
              super().info()
              print ("Dog is bark")

s=Dog()
s.info()
h = V_human()
h.info()






