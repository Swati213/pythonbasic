from Tkinter import *


app = Tk()
options=["Python","PHP","Android","ASP.NET","Bootstrap"]
fees={"Python":5500,"PHP":5500,"Android":5000,"ASP.NET":7000,"Bootstrap":3500}

def on_op_select(event):
    course = op_data.get()
    data="Fee of {0} is {1}".format(course,fees[course])
    fee_label.config(text=data)
#OptionMenu Demo
op_data=StringVar()
op_data.set("Select Option")

op_menu=OptionMenu(app,op_data,*options,command=on_op_select)
fee_label=Label(app,text="Fee : ");


op_menu.grid(row=0,column=0)
fee_label.grid(row=1,column=0)


app.mainloop()
