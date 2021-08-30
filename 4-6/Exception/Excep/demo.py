try:
    num_one = input("Enter 1st Number : ")
    num_two = input("Enter 2nd Number : ")
    num_one = int(num_one)
    num_two = int(num_two)
except:
    print ("ValueError")
else:
    try:
        res = num_one / num_two
    except:
        print ("Zeero Division Error")
    else:
        print ("Result :",res)

