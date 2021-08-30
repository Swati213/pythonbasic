#multiple Inheritance
class LoanCalculator :
    def __init__(self):
        self.intrest = 4
    def calculateIntrest(self, amunt, time ):
        return amunt * (1+self.intrest*time)
class SimpleCalculator :
    def __init__(self):
        self.result = 0
    def add (self, num):
        self.result += num
    def sub (self, num):
        self.result -=num
class ScientificCalculator (SimpleCalculator,LoanCalculator ):
    def __init__(self):
        LoanCalculator . __init__(self)
        SimpleCalculator . __init__(self )
    def squre (self, num):
        self.result = num*num


a = ScientificCalculator ()
a.add(2)
print a.result
a.sub(3)
print a.result
a.squre(4)
print a.result
a.sub(4)
print a.result
a.add(5)
print a.result
print a. calculateIntrest(2000,1)

    
        
