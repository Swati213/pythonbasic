"""multiple inheritance"""
class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showdata(self):
        print("name",self.name)
        print("age",self.age)
        print("hello!!!!")
class b:
    def __init__(self,roll):
        self.roll=roll
    def showdata1(self):
        print("roll",self.roll)
        print("hi there!!!!")
class c(a,b):
    def __init__(self,name,age,roll,marks):
        a.__init__(self,name,age)
        b.__init__(self,roll)
        self.marks=marks
    def showdata2(self):
        a.showdata(self)
        b.showdata1(self)
        print("marks",self.marks)
        print("hi !!!!")
obj1=a("suman singh",56)
obj1.showdata()
obj2=b('45005')
obj2.showdata1()
obj=c("Raima kanna",23 ,'40007',890)
obj.showdata2()




    
