#with using aggregation inheritan
class Driver :
       def __init__ (self,dname,dage,daddr):
              self.dname =dname
              self.dage = dage
              self.daddr=daddr
              

class Car:
       def __init__(self,cname,cmodel,dname,dage,daddr):
              self.cname=cname
              self.cmodel=cmodel
              self.obj_driver = Driver(dname,dage,daddr)
       def show(self):
              print ("Car Name : ", self.cname)
              print ("Car Model : ",self.cmodel)
              print ("Driver Name : ",self.obj_driver.dname)
              print ("Driver's Age : ",self.obj_driver.dage)
              print ("Driver'address : ",self.obj_driver.daddr)

d = Car("Hyndai","i20","Jhon",25,"Civil lines" )
d.show()

d1 = Car("Hyndai","i20","Rahul",35,"Civil lines" )
d1.show() 
