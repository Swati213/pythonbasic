class grandfather:
    def __init__(self):
        self.name="Ram singh"
        self.age=79
    def display(self):
        print("grandpa name:",self.name)
        print("grandpa age:",self.age)
        print("hello grandfather")
class father:
    def details(self):
        self.name="sanjay singh"
        self.age=57
    def display1(self):
        print("father name:",self.name)
        print("father age:",self.age)
        print("hello father")
class son(grandfather,father):
    def details(self):
        grandfather.__init__(self)
        father.__init__(self)
        self.name="suraj singh"
        self.age=34
    def display2(self):
        grandfather.display(self)
        father.display1(self)
        print("son name:",self.name)
        print("son age:",self.age)
        print("hello son")
class  grandson(son):
    def details(self):
        son.__init__(self)
        self.name="Tanmay singh"
        self.age=7
    def display3(self):
        son.display2(self)
        print("grandson name:",self.name)
        print("grandson age:",self.age)
        print("hello  grandson")
obj=grandson()
obj.display3()



    

    
    































































































    
