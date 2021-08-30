"""constructor and deconstructor"""
class emp:
    company="Tata hill pvt lmt"
    def __init__(self):
        self.emp_name=input("enter a name")
        self.emp_age=input("enter the age")
        self.emp_department=input("enter department")
        self.emp_role=input("enter role")
    def setdata(self):
        self.emp_wages=input("enter the salary")
        self.emp_company=emp.company    
    def show(self):
        print("emp_name: {0} \n emp_age:{1}\n emp_department:{2} \n emp_role:{3} \n emp_wages:{4}".format(self.emp_name,self.emp_age,self.emp_department,self.emp_role,self.emp_wages))
        print("emp_company:",self.emp_company)
    def __del__(self):
        print("deconstructor")
obj=emp()
obj1=emp()
obj.setdata()
obj.show()
obj1.show()
del obj
obj.show()
        
            
