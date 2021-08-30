from tkinter import *
from time import *

app = Tk()



dateLbl = Label(app,text=strftime("%d"),font=("cooper black",50))
timeLbl = Label(app,text=strftime("%I:%M:%S %p"),font=("cooper black",20))

dateLbl . pack()
timeLbl . pack()
app.mainloop()
