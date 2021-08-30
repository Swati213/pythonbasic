from threading import *
def display():
    print("hello their\n")
for i in range(5):
    t=Thread(target=display)
    t.start()

