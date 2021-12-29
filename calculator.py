
from tkinter import *
from datetime import date

root=Tk()   
root.title("Accurate Age Calculator App")    
root.geometry("400x300")   
new=Label(root)  
new.grid(row=5,column=0,columnspan=3)

today=str(date.today())    
list_today=today.split("-")  

def age(b_date,b_month,b_year):
    global today
    global new
    new.grid_forget()
    b_date=int(entry_date.get())
    b_month=int(entry_month.get())
    b_year=int(entry_year.get())
    c_date=int(list_today[2])
    c_month=int(list_today[1])
    c_year=int(list_today[0])
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>c_date):
        c_month=c_month-1
        c_date=c_date+month[b_month-1]
    if (b_month>c_month):
        c_year=c_year-1
        c_month=c_month+12
    resultd=str(c_date-b_date)
    resultm=str(c_month-b_month)
    resulty=str(c_year-b_year)
    new=Label(root,text="YOUR AGE IS\n"+resulty+" YEARS "+resultm+" MONTHS AND "+ resultd+" DAYS",borderwidth=6)
    new.config(font=("Arial Rounded MT Bold",15))
    new.grid(row=5,column=0,columnspan=3)


def clean(entry_date,entry_month,entry_year):
    global new
    new.grid_forget()
    entry_date.delete(0,END)
    entry_month.delete(0,END)
    entry_year.delete(0,END)

title_label=Label(root,text="ACCURATE AGE CALCULATOR APP",borderwidth=10)
title_label.config(font=("Broadway",15))
title_label.grid(row=0,column=0,columnspan=3)
label_date=Label(root,text="BIRTH DATE : ",borderwidth=4)
label_date.config(font=("Arial Rounded MT Bold",15))
label_date.grid(row=1,column=0)
label_month=Label(root,text="BIRTH MONTH : ",borderwidth=5)
label_month.config(font=("Arial Rounded MT Bold",15))
label_month.grid(row=2,column=0)
label_year=Label(root,text="BIRTH YEAR : ",borderwidth=9)
label_year.config(font=("Arial Rounded MT Bold",15))
label_year.grid(row=3,column=0)

entry_date=Entry(root,width=20,borderwidth=3)
entry_month=Entry(root,width=20,borderwidth=3)
entry_year=Entry(root,width=20,borderwidth=3)

entry_date.grid(row=1,column=2)
entry_month.grid(row=2,column=2)
entry_year.grid(row=3,column=2)


b_date=entry_date.get()
b_month=entry_month.get()
b_year=entry_year.get()


submit=Button(root,text="GET AGE!!",width=10,anchor=CENTER,command=lambda:age(b_date,b_month,b_year), borderwidth=5)
submit.grid(row=4,column=0)


clear=Button(root,text="CLEAR",width=10,command=lambda:clean(entry_date,entry_month,entry_year),borderwidth=5)
clear.grid(row=4,column=2)

root.mainloop()



