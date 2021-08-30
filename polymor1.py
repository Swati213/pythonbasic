#without using opreator overloading
"""
class Product :
       def __init__(self,pro_name,rs):
              self.pro_name=pro_name
              self.rs=rs
       def item (self,Product):
              return self.rs + Product.rs



p = Product("Pepsi", 90)
p1= Product ("Pepsi",65)
print (p.item(p1))
       
"""

#with using opreatoroverloading

class Product :
       def __init__(self,pro,rs):
              self.pro = pro
              self.rs = rs
       def __add__(self,Product):
              return self.rs + Product.rs
p1=Product("Item 1",7)
p2=Product("Item 2",30)
print (p1+p2)

       
