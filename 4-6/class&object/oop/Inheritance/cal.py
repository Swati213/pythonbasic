class Cal:
    def add(self, none, ntwo):
        return none + ntwo

    def sub(self, none, ntwo):
        return none - ntwo

class Scical:
    def __init__(self):
        self.cal = Cal()
    def fact(self, num):
        if num is 0:
            return 1
        else:
            return num * self.fact(num-1)

obj = Cal()
sciObj = Scical()

#print obj.add(2, 4)
#print obj.sub(5, 2)
#print sciObj.fact(5)
#print sciObj.cal.add(3, 5)


