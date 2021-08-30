class Demo:
    message = "Spectrum"

    def __init__(self):
        print "Constructor"

    def __del__(self):
        print "Destructor"

    def __str__(self):
        return "Demo Class"
        
    def show_msg(self):
        print "ShowMsg Method"

    @staticmethod
    def stmethod(data):
        print "stmethod : ",data
        
 #print Demo.message
first_obj = Demo()
print first_obj 
del first_obj
 first_obj . show_msg()
# Demo . show_msg(first_obj)
Demo . stmethod(34)  
