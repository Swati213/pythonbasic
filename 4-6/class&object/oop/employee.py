class Employee:
    organization = "Spectrum"
    def __init__(self, emid, emname, emsalary):
        self.emp_id = emid
        self.emp_name = emname
        self.emp_salary = emsalary
        
    def show_info(self):
        print "Emp ID : ", self.emp_id
        print "Emp Name : ", self.emp_name
        print "Emp Salary : ", self.emp_salary
        print "Organization : ", Employee.organization
        

"""emp_one = Employee("Spec001","Prakash", 10000)#will create an object
emp_one.show_info()
emp_two =  Employee("Spec002")
#print emp_one.show_info()
print emp_two.show_info()

emp_one.emp_id="spec1001"
emp_one.emp_name="Prakash"
emp_one.emp_salary=10000



hasattr()   : will check existence of specified attribute and return True or False
setattr() : will change or add specified attribute
getattr() : will return value of specified attribute
delattr() : will delete specified attribute from object
"""

"""
emp_two.emp_name="Praveen"
emp_two.emp_salary=12000
"""

emp_one = Employee("Spec001","Prakash", 10000)
print (emp_one.__dict__)
#print hasattr(emp_one, "addrs")
#setattr(emp_one, "emp_name", "Praveen")
#print emp_one.show_info()
#setattr(emp_one, "emp_salary", 8000)
#print emp_one.show_info()
#delattr(emp_one,"emp_salary")
#print emp_one.show_info()
print getattr(emp_one,"emp_address", "Not Found")
#emp_one.show_info()
#emp_two.show_info()

