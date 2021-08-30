class student:
    """class variable"""
    school="sjc sch"
    def __init__(self,sid,sname=0,smarks=0):
        self.stu_id=sid
        self.stu_name=sname
        self.stu_marks=smarks
    def show_info(self):
        print("id:",self.stu_id)
        print("name:",self.stu_name)
        print("marks:",self.stu_marks)
        print("school:",student.school)
a=input("enter the id")
b=input("enter the name")
c=input("enter the marks")
stu_obj=student(a,b,c)
stu_obj.show_info()
        
    
    
