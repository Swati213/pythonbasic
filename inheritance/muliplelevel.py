"""muliplelevel inheritance"""
class student:
    def getstudent(self):
        self.name=input("name:")
        self.age=input("age:")
        self.gender=input("gender:")
class test(student):
    def getmarks(self):        
        self.stuclass=input("class:")
        print("enter the marks of respective subject")
        self.english=input("english:")
        self.maths=input("maths:")
        self.hindi=input("hindi:")
        self.science=input("science:")
        self.socialscience=input("socialscience:")
        self.table=self.english+self.maths+self.hindi+self.science+self.socialscience
        
class marks(test):
    def display(self):
        #super().getstudent()
        print("\n\n Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Student class:",self.stuclass)
        print("total marks:",self.table)
        
m1=marks()
m1.getstudent()
m1.getmarks()
m1.display() 
    





