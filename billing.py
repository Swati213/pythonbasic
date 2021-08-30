from tkinter import *
a = Tk()
a.title ("SHOP INFO")
a.iconbitmap("shops.ico")

def calculateTotal(event):
    data_one = rate1_box.get()
    data_two = rate2_box.get()
    data_three = rate3_box.get()
    data_four = rate4_box.get()
    data_five = rate5_box.get()
    if (event.widget==rate1_box):
        data_one = rate1_box.get()+event.char
    if (event.widget==rate2_box):
        data_two = rate2_box.get()+event.char
    if (event.widget==rate3_box):
        data_three = rate3_box.get()+event.char
    if (event.widget==rate4_box):
        data_four = rate4_box.get()+event.char
    if (event.widget==rate5_box):
        data_five = rate5_box.get()+event.char

    if (len(data_one)==0):
        data_one =0
    else:
        data_one = int(data_one)
    if (len(data_two)==0):
        data_two =0
    else:
        data_two = int(data_two)
    if (len(data_three)==0):
        data_three =0
    else:
        data_three = int(data_three)
    if (len(data_four)==0):
        data_four =0
    else:
        data_four = int(data_four)
    if (len(data_five)==0):
        data_five =0
    else:
        data_five = int(data_five)

    res = data_one+data_two+data_three+data_four+data_five
    total_box.delete(0,END)
    total_box.insert(INSERT,res)

def discount (event):
    g = int  (total_box.get())
    h = int  (discount_box.get()+event.char)
    
    grand = g - ((g*h)/100)
    grand_box.delete(0,END)
    grand_box.insert(INSERT,grand)

shop_name = Label(a,text = "KAPOOR GARMENT", fg = "red")
shop_add = Label(a,text = "1,kotha Parcha,Alld", fg = "red")
shop_mobile = Label(a,text = "0987654321", fg = "red")
shop_state = Label(a,text = "Uttar Pradesh", fg = "red")
cuname_label = Label(a,text = "Customer Name" , fg = "white" , bg = "black")
cuname_box = Entry(a)
mobile_label = Label(a,text = "Customer mobile no." , fg = "white" , bg = "black")
mobile_box = Entry(a)
total_label = Label(a,text = "Total Amount" , fg = "white" , bg = "black")
total_box = Entry(a)
item_label = Label(a,text = "ITEM", fg = "red")
name_label = Label(a,text = "NAME", fg = "white", bg = "black").grid(row =10 , column =1, padx =8 , pady =8 , ipadx =5 , ipady =5)
rate_label = Label(a,text = "RATE", fg = "white", bg = "black").grid(row =10 , column =2 , padx =8 , pady =8 , ipadx =5 , ipady =5)
discount_label = Label(a,text = "DISCOUNT", fg = "white", bg = "black").grid(row =17 , column =1 , padx =8 , pady =8 , ipadx =5 , ipady =5)
discount_box = Entry(a)
discount_box.grid(row =17 , column =2 , padx =8 , pady =8 , ipadx =5 , ipady =5)
discount_box.bind("<Key>",discount)
grand_label = Label(a,text = "GRAND TOTAL", fg = "white", bg = "black").grid(row =18 , column =1 , padx =8 , pady =8 , ipadx =5 , ipady =5)
grand_box = Entry(a)
grand_box.grid(row =18 , column =2 , padx =8 , pady =8 , ipadx =5 , ipady =5)
pay_label = Label(a,text = "PAY BILL AMOUNT", fg = "white", bg = "black").grid(row =19 , column =1 , padx =8 , pady =8 , ipadx =5 , ipady =5)
pay_box = Entry(a).grid(row =19 , column =2 , padx =8 , pady =8 , ipadx =5 , ipady =5)
b_label = Label(a,text = 1).grid(row =11 , column =0)
itemname1_box = Entry(a).grid(row = 11 , column = 1)
rate1_box = Entry(a)
rate1_box.grid(row = 11 , column = 2)
c_label = Label(a,text = 2 ).grid(row =12 , column = 0)
itemname2_box = Entry(a).grid(row = 12 , column = 1)
rate2_box = Entry(a)
rate2_box.grid(row = 12 , column = 2)
d_label = Label(a,text = 3 ).grid(row =13 , column = 0)
itemname3_box = Entry(a).grid(row = 13 , column = 1)
rate3_box = Entry(a)
rate3_box.grid(row = 13 , column = 2)
e_label = Label(a,text = 4 ).grid(row =14 , column = 0)
itemname4_box = Entry(a).grid(row = 14 , column = 1)
rate4_box = Entry(a)
rate4_box.grid(row = 14 , column = 2)
f_label = Label(a,text = 5 ).grid(row =15 , column = 0)
itemname5_box = Entry(a).grid(row = 15 , column = 1)
rate5_box = Entry(a)
rate5_box.grid(row = 15 , column = 2)
shop_name.grid(row =0 , column =1 , padx =6 , pady =6 )
shop_add.grid(row =1 , column =1 , padx =6 , pady =6 )
shop_mobile.grid(row =2 , column =1 , padx =6 , pady =6 )
shop_state.grid(row =3 , column =1 , padx =6 , pady =6 )
cuname_label.grid(row = 4 , column = 0 , padx = 6 , pady = 6 , ipadx = 7 , ipady = 7)
cuname_box.grid(row = 4 , column = 1 , padx = 4 , pady = 4 , ipadx = 6 , ipady = 6)
mobile_label.grid(row = 5 , column = 0 , padx = 2 , pady = 2 , ipadx = 6 , ipady = 6)
mobile_box.grid(row = 5 , column = 1 , padx = 4 , pady = 4 , ipadx = 6 , ipady = 6)
total_label.grid(row = 16 , column = 1 , padx = 4 , pady = 4 , ipadx = 5 , ipady = 5)
total_box.grid(row = 16 , column = 2  , padx = 4 , pady = 4 , ipadx = 5 , ipady = 5)
rate1_box.bind("<Key>",calculateTotal)
rate2_box.bind("<Key>",calculateTotal)
rate3_box.bind("<Key>",calculateTotal)
rate4_box.bind("<Key>",calculateTotal)
rate5_box.bind("<Key>",calculateTotal)
item_label.grid(row = 9 , column = 1, padx = 4, pady = 4, ipadx = 5 , ipady = 5)

a.mainloop()
