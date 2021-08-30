class Book:
    """ Class Book: My Book Class """
    no_of_books = 0 # class variable
    def __init__(self):
        # instance variables
        self.book_name = None
        self.author = None
        self.publication = None
        self.pages = 0

    def show_info(self):
        print "Information"

    def  show_msg(self, msg):
        print "Message : ",msg


obj = Book()
"""
print Book.no_of_books
print hasattr(obj, "pages")
print getattr(obj, "prs", "not found")
setattr(obj, "book_name","Let us C")
delattr(obj, "book_name")
print obj.book_name
"""
obj.show_msg("Hello")
Book.show_msg(obj, "Spectrum")
print Book.__name__
print Book.__module__
print Book.__bases__
print Book.__doc__
print Book.__dict__



