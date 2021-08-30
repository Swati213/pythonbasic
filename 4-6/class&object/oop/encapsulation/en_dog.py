class Dog:
    species = 'mammal'#(class attribute, class varriable)
    def __init__(self, name, age): # built in function
        self.name = name # instance varriable 
        self.age = age # instance varriable 
    def description(self): # user define function
        return "{} is {} years old".format(self.name, self.age)
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)



mikey = Dog("Mikey", 6)

# call our instance methods
print mikey.description()
print mikey.speak("Gruff Gruff")
