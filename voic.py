"""import pyttsx3
for attr in dir(pyttsx3):
    print (attr)
"""
from pyttsx3 import*
def myspeak(message):
    engine=init()
    engine.say('{}'.format(message))
    engine.runAndWait()

#message='''hello how are you?'''
message = input("Please enter any word :")
myspeak(message)
