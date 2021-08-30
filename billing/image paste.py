from Tkinter import *
from PIL import image, ImageTk
b = Tk()
img = Image.open("check-mark.png")
tkimage = ImageTk.PhotoImage(img)
img_label = Label(b.image = tkimage).pack()
b.iconbitmap("check-mark.ico")
b.mainloop()
