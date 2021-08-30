def get_fact(num):
    if num is 0 :
        return 1
    else :
        return num * get_fact(num-1)



def fact(num):
    if num is 0 :
        return 1
    else :
        res=num
        for n in range(num-1,0,-1):
            res *= n
        return res

#result = get_fact(5)
#print "Result :",result

print "Res :",fact(4)






