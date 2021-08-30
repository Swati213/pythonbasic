class employee:
    "enployee personal information"
    def personal(self):
        "personal info"
        self.name="Ramesh kumar"
        self.fathersname="Sagar kumar"
        self.age=23
        self.date_of_birth="23/6/1991"
        self.education="MBA"
        print("name: ",self.name)
        print("fathersname:",self.fathersname)
        print("date of birth:",self.date_of_birth)
        print("age:",self.age)
        print("education:",self.education)
    def professional(self):
        "professional info"
        self.salary=50000
        self.role="HR"
        self.gmail="ramesh34@gmail.com"
        print("salary:",self.salary)
        print("role:",self.role)
        print("gmail:",self.gmail)
e=employee()
e.personal()
e.professional()        
    
