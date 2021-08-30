"""
Syntax
class Classname (BaseClassName,):
    'Documentation String'
    Members....
"""
class Cal:
    def add(self, none, ntwo):
        return none + ntwo

    def sub(self, none, ntwo):
        return none - ntwo

class Scical(Cal):
    def fact(self, num):
        if num is 0:
            return 1
        else:
            return num * self.fact(num-1)

sciObj = Scical()
print sciObj.add(2, 7)

