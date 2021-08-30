try:
    import myrandom
    int("spec1232")
except ImportError as err:
    print (err)
except Exception as err:
    print (err)
else:
    print (random.randint(1,1000))
finally:
    print ("End!!!!")
