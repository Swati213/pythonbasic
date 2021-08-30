def add_data(num, *number):
    res = num
    for n in number :
        res += n #res = res +n
    print "Result :",res
    print type(number)
#add_data(3,5,6)
#add_data(3,8)   

def aa (*name):
    print name


aa("Monika", "Sonu")

    
def show_info(**info):
    #print name
    print info
    print type(info)
    

#show_info(email="prakash@mail.com", age=25, mobile="97626262",address="civil lines")
