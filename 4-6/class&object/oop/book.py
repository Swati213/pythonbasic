class Book:
    """ Class Book """
    no_of_books = 0 # class variable
    def __init__(self):
        # instance variables
        self.book_name = "Let us C"
        self.author = "Sumith Sharma"
        self.publication = "J.B. publication"
        self.pages = "350"
        print self.book_name
        print self.author
        print self.publication
        #print self.pages
        #print self.book_name,self.author,self.publication,self.pages
        #print "Book Name = {0}\n Author Name = {1}\n Publication Name = {2} \n No. of Pages = {3}".format(self.book_name,self.author,self.publication,self.pages)

    def show_info(self):
        print "Information"

# Object Creation
obj = Book()

obj.book_name
#obj.author = "abc"
#obj.publication = "mno"
#obj.pages = 250

#obj.show_info()
#print "Name : ",obj.book_name

