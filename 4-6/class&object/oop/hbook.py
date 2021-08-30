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
obj.show_info()
print hasattr(obj, "pages")
print getattr(obj, "prs", "not found")
setattr(obj, "book_name","Let us C")
print obj.book_name
delattr(obj, "book_name")
print obj.book_name
