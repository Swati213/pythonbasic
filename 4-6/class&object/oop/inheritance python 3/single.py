class info :
       def __init__(self, Id, name):
              print ("Hello.....")
              self.Id = Id
              self.name = name
       def show(self):
              print ("Id no: ",self.Id)
              print ("Std Name: ",self.name)

class std_info(info):
       def __init__(self,school,Id,name,per):
              self.school = school
              info.__init__(self,Id,name)
              self.per = per
       def display(self):
              print("School Name: ", self.school)
              info.show(self)
              print("Total Pertcentage: ",self.per)
            
              


#p=info(12, "Rahul")
#p.show()
s=std_info("GIC SCHOOL", 10, "Mohan", 60)
s.display()
#s.show()




