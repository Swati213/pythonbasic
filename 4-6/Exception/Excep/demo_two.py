try:
    num_e = input("Enter 1st Number : ")
    num_two =input("Enter 2nd Number : ")
    num_one = int(num_one)
    num_two = int(num_two)
    res = num_one / num_two
except ValueError as err:
    print (err)
except ZeroDivisionError as err:
    print (err)
except Exception as err:
    print (err)
else:
    print ("Result :",res)

