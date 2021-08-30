from tkinter import*
app =Tk()
def show ():
    print ("Hello India....!")
def close ():
    exit()
    
first_lbl = Label(app, text = "Hello Firends.....", fg = "Green" )
first_lbl.pack (side = "top")

last_buton = Button (app, text = "Exit", fg = "Red", command = close)
last_buton.pack(side = "bottom")

first_buton = Button (app, text = "Click here", fg = "Blue", command = show)
first_buton.pack(side = "bottom" )

app.mainloop()
