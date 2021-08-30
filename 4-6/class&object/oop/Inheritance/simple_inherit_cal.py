class Calculator :
    def add (self, num_one, num_two):
        return num_one + num_two
    def sub (self, num_one, num_two):
        return num_one - num_two


class Scientific (Calculator):
    def fact (self, num) :
        if num == 0 :
            return 1
        else :
            return num * self.fact (num - 1)



#c = Calculator()
s = Scientific ()
print s.fact(5)
print s.add(3,5)
print s.sub (4,2)
        
        
