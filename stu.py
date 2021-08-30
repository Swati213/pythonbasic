class student:
    """class variable"""
    roll=23
    age=23
    def __init__(self):
        """global variable"""
        self.tot_marks=0
        self.percent=0
        """instance variable"""
        self.name="Ajay gupta"
        self.d_o_b="7/8/1996"
        self.age=student.age
        self.parent_name="Sumith gupta"
        self.collage_name="J.K.COLLAGE"
        self.department="IPS"
        self.stream="MCA"
        self.enroll_no="8000768"
        self.roll_no=student.roll
        self.gmail="ajay796gupta@gmail.com"
    def getdata(self):
        self.subject=["Artificial Intelligence","Data Mining","Digital Communication","Image Processing","Computer Security"]
        self.marks=[67,89,56,74,54]
        for i in range(0,len(self.marks)):
            self.tot_marks=self.tot_marks + self.marks[i]
        self.percent=self.tot_marks/5
        
    def printdata(self):
        print("name:{0} \n d_o_b:{1} \n age:{2} \n parent_name:{3}\n collage_name:{4}\n department:{5} \n stream:{6}\n enroll_no:{7}\n roll_no:{8} \n gmail:{9} ".format(self.name,self.d_o_b,self.age,self.parent_name,self.collage_name,self.department,self.stream,self.enroll_no,self.roll_no,self.gmail))
        print("subject:",self.subject)
        print("marks:",self.marks)
        print("total marks:",self.tot_marks)
        print("percentage:",self.percent)
obj=student()
obj.getdata()
obj.printdata()
print("student.__doc__:",student.__doc__)
print("student.__name__:",student.__name__)
print("student.__bases__:",student.__bases__)
print("student.__module__:",student.__module__)
print("student.__dict__:",student.__dict__)
print (obj.__dict__)



    





