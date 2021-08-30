from tkinter import *
app = Tk()
app.title("Calculator")
app.configure(background="light green")

def press (event):
    btn = event.widget
    text = btn.config("text")[4]
    oldText=str(en.config("text")[4])
    if text == "Clear" :
        en.config(text = "")
    elif text == "=":
        for ch in ("+","-","*","/","%") :
            oldText = oldText . strip(ch)
        else :
            result = eval(oldText)
            en.config(text=result)
    else :
        if ( oldText.endswith("+") or oldText.endswith("-") or oldText.endswith("*") or oldText.endswith("/") or oldText.endswith("%") ) and ( text in ("+","-","*","/","%")) :
            pass
        else :
            newText = oldText + text
            #print (text)
            en.config(text = newText)

en= Label (app,background="yellow", width = 50, foreground="blue")
en.grid (row = 0 , columnspan = 5)

b1 = Button (app, background = "red", text = "1", fg = "yellow", width = 10)
b1.grid (row = 1 , column = 0, padx=8, pady=8)

b2 = Button (app, background = "red", text = "2", fg = "yellow", width = 10)
b2.grid (row = 1 , column = 1, padx=8, pady= 8)

b3 = Button (app, background = "red", text = "3", fg = "yellow", width = 10)
b3.grid (row = 1 , column = 2, padx=8, pady= 8)

b_equal = Button (app, background = "red", text = "=", fg = "yellow", width = 10)
b_equal.grid (row = 1 , column = 3, padx=10, pady=10)

b4 = Button (app, background = "red", text = "4", fg = "yellow", width = 10 )
b4.grid (row = 2 , column = 0, padx=8, pady= 8)

b5 = Button (app, background = "red", text = "5", fg = "yellow", width = 10)
b5.grid (row = 2 , column = 1, padx=8, pady= 8)

b6 = Button (app, background = "red", text = "6", fg = "yellow", width = 10)
b6.grid (row = 2 , column = 2, padx=8, pady= 8)

b_plus = Button (app, background = "red", text = "+", fg = "yellow", width = 10)
b_plus.grid (row = 2 , column = 3, padx=8, pady= 8)

b7 = Button (app, background = "red", text = "7", fg = "yellow", width = 10)
b7.grid (row = 3 , column = 0, padx=8, pady= 8)

b8 = Button (app, background = "red", text = "8", fg = "yellow", width = 10)
b8.grid (row = 3 , column = 1, padx=8, pady= 8)

b9 = Button (app, background = "red", text = "9", fg = "yellow", width = 10)
b9.grid (row = 3 , column = 2, padx=8, pady= 8)

b_sub = Button (app, background = "red", text = "-", fg = "yellow", width = 10)
b_sub.grid (row = 3 , column = 3, padx=8, pady= 8)

b0 = Button (app, background = "red", text = "0", fg = "yellow", width = 10)
b0.grid (row = 4 , column = 0, padx=8, pady= 8)

b_persent = Button (app, background = "red", text = "%", fg = "yellow", width = 10)
b_persent.grid (row = 4 , column = 1, padx=8, pady= 8)

b_multiple = Button (app, background = "red", text = "*", fg = "yellow", width = 10)
b_multiple.grid (row = 4 , column = 2, padx=8, pady= 8)

b_clear = Button (app, background = "red", text = "Clear", fg = "yellow", width = 10)
b_clear.grid (row = 4 , column = 3, padx=8, pady= 8 )

b1.bind("<Button-1>",press)
b2.bind("<Button-1>",press)
b3.bind("<Button-1>",press)
b_equal.bind("<Button-1>",press)
b4.bind("<Button-1>",press)
b5.bind("<Button-1>",press)
b6.bind("<Button-1>",press)
b_plus.bind("<Button-1>",press)
b7.bind("<Button-1>",press)
b8.bind("<Button-1>",press)
b9.bind("<Button-1>",press)
b_sub.bind("<Button-1>",press)
b0.bind("<Button-1>",press)
b_persent.bind("<Button-1>",press)
b_multiple.bind("<Button-1>",press)
b_clear.bind("<Button-1>",press)

app.mainloop()
