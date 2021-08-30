from googletrans import *
try :
    translator = Translator ()
    data = raw_input ("Enter the Text : ")
    lang_Code = raw_input ("Enter the lang. Code : ")
    result = translator.translate(data, lang_Code)
except Exception as err:
    print "Error",err
else:
    print "Translate text : ", result.text
