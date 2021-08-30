class Demo:
    message = "Spectrum"

    def __init__(self):
        print "Constructor"
    def show(self):
        print "Hello Rahul"

    def __del__(self):
        print "Destructor"


first_obj = Demo()
first_obj.show()
del first_obj
print first_obj
