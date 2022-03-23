

from tkinter import*
import math
calc=Tk()
calc.title('calculator')
calc.geometry('640x500')
calc.configure(bg='burlywood')
#calc.attributes('-fullscreen',True)
title=Label(calc,text='CALCULATOR',padx=50,font=('times','30','bold italic'),fg='gray',bg='burlywood')
title.grid(row=0,column=2)

value1=Label(text='value1:',font=('times','30','bold italic'),bg='burlywood',padx=20)
value1.grid(row=1,column=1,sticky='w')
E1=Entry(bd=5,relief=GROOVE)
E1.grid(row=1,column=2)

value2=Label(text='value2:',font=('times','30','bold italic'),bg='burlywood',padx=20)
value2.grid(row=2,column=1,sticky='w')
E2=Entry(bd=5,relief=GROOVE)
E2.grid(row=2,column=2)

value3=Label (font=('times','20','italic'),width=20,pady=20,bg='burlywood')
value3.grid(row=3,column=1)


def add():
    addition=int(E1.get())+int(E2.get())
    #print(addition)
    #value3.config(text=addition)
    value3.config(text='the sum is='+str(addition))
    
add1=Button(text='+',font=('times','30','bold italic'),bg='gray',command=add)
add1.grid(row=3,column=2)

def sub():
    subtraction=int(E1.get())-int(E2.get())
    #print(subtraction)
    value3.config(text='the subtract is='+str(subtraction))

sub2=Button(text='-',font=('times','30','bold italic'),bg='gray',command=sub)
sub2.grid(row=4,column=2)

def mul():
    multiply=int(E1.get())*int(E2.get())
    #print(multiply)
    value3.config(text='the cross product='+str(multiply))

multiply3=Button(text='*',font=('times','30','bold italic'),bg='gray',command=mul)
multiply3.grid(row=5,column=2)

def div():
    divide=int(E1.get())/int(E2.get())
    #print(divide)
    value3.config(text='division ='+str(divide))

divide4=Button(text='/',font=('times','30','bold italic'),bg='gray',command=div)
divide4.grid(row=6,column=2)

btn=Button(calc,text='EXIT calculator',command=calc.destroy,bg='powder blue',fg='blue',activebackground='pink')
btn.grid(row=6,column=1,pady=10,)

calc.mainloop()
