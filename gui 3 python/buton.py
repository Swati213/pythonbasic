from tkinter import *
from PIL import Image,ImageTk
app = Tk()
app.title ("my photo")
img = Image.open("images.jpg")
photo = ImageTk.PhotoImage (img)
labl = Label (app, image = photo)
labl.grid (row = 0, column = 0, stick = E)
app.mainloop ()
