class VoteError(Exception):
    def __init__(self, user):
        Exception.__init__(self)
        self.user = user
    def __str__(self):
        return "Dear {0}, you are underage!!!!".format(self.user.name)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def vote(self):
        if self.age >= 18 :
            print ("Done")
        else:
            #raise(ValueError("You are underage!!!!"))
            raise(VoteError(self))

obj = User("Prakash",12)
try:
    obj.vote()
except Exception as err:
    print (err)
        
