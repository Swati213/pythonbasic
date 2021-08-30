from tkinter import *
from PIL import ImageTk, Image
a = Tk()


a.iconbitmap("ff.ico")
img = ImageTk.PhotoImage(Image.open("Chrysanthemum.jpg"))

lb=Label(a,image=img)
lb.pack(fill=BOTH, expand=TRUE)
a.mainloop()
