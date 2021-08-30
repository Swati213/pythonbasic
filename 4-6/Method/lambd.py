def squ (a):
    return a*a

result = squ(5)
print result


f = lambda a:a*a
res = f(5)
print res

"""

f = lambda a,b: a+b
res= f(6,8)
print res
"""


def even (n):
    return n%2==0

num = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(even,num))
print evens













