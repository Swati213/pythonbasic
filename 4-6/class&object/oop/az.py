class test :
    "documentation class"
    roll_no =1
    marks = 56
    def __init__(self):
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print "Roll no : ",self.roll_no
        print "Marks : ",self.marks


print "Test.__doc__:",test.__doc__
print "Test.__name__:",test.__name__
print "Test.__bases__:",test.__bases__
print "Test.__module__:",test.__module__
print "Test.__dict__:",test.__dict__
    
