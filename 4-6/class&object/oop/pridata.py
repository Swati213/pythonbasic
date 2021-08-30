class PrivateData:
    __mydata = "Spectrum"
    def __init__(self):
        self.__name="kk"

    def show_data(self):
        print PrivateData.__mydata
        print self.__name


#print PrivateData.__mydata
obj = PrivateData()

obj . show_data()
print obj.__name
#print obj._PrivateData__mydata
