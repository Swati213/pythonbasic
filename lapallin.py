a=input("enter a string")
l=list(map(lambda x:(x==" ".join(reversed(x))),a))
if(a==l):
    print("string is pallindrome",a)
else:
    print("string is not pallindrome",a)

    
