from tkinter import *
a = Tk()

#def show():
   # a = int (a_box.get())
#    b = int(b_box.get())
    #c = int(c_box.get())
    #box = a+b+c
    #total_box.insert(INSERT,box)

def calculateTotal(event) :
    data_one=a_box.get()
    data_two=b_box.get()
    data_three=c_box.get()
    if(event.widget==a_box) :
        data_one = a_box.get() +event.char
    if(event.widget==b_box) :
        data_two= b_box.get() +event.char
    if(event.widget==c_box) :
        data_three = c_box.get() +event.char

        
    if(len(data_one)==0):
        data_one = 0
    else :
        data_one=int(data_one)
    if(len(data_two)==0):
        data_two = 0
    else :
        data_two=int(data_two)
    if(len(data_three)==0):
        data_three = 0
    else :
        data_three=int(data_three)

    res=data_one+data_two+data_three
    total_box.delete(0,END)
    total_box.insert(INSERT,res)

def discount (event):
    d = int (total_box.get())
    e = int (discount_box.get()+event.char)
    
    tpa = d -((d* e)/100)
    tpa_box.delete(0,END)
    tpa_box.insert(INSERT,tpa)

a.title("shop name")
a_box = Entry(a)
a_box . grid(row =0 , column =1 , padx =8 , pady =8 , ipadx =5 , ipady =5)
b_box = Entry(a)
b_box . grid(row =1 , column =1 , padx =4 , pady =4 , ipadx =4 , ipady =4)
c_box = Entry(a)
c_box . grid(row =2 , column =1 , padx =4 , pady =4 , ipadx =4 , ipady =4)
lable_1 = Label(a,text = "Total")
lable_1 . grid(row = 3 , column = 1)
total_box = Entry(a)
total_box . grid(row =4 , column =1 , padx =4 , pady =4 , ipadx =4 , ipady =4)
a_box.bind("<Key>",calculateTotal)
b_box.bind("<Key>",calculateTotal)
c_box.bind("<Key>",calculateTotal)

lable_2 = Label(a,text = "Discount ")
lable_2 . grid(row = 5 , column = 1)
discount_box = Entry(a)
discount_box . grid(row =6 , column =1 , padx =4 , pady =4 , ipadx =4 , ipady =4)
discount_box.bind("<Key>",discount)

lable_2 = Label(a,text = "Total Pay Amount ")
lable_2 . grid(row = 7 , column = 1)
tpa_box = Entry(a)
tpa_box . grid(row =8 , column =1 , padx =4 , pady =4 , ipadx =4 , ipady =4)


    


a.mainloop()
