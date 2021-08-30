"""import googletrans
print dir(googletrans)
for r in dir(googletrans):
    print r"""

from googletrans import *
data = raw_input("Enter String : ")
code = raw_input("Enter code : ")
translator = Translator()
res = translator.translate(data,code )
print "translate word : ",res.text


