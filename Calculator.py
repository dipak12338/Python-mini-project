from tkinter import *
root=Tk()
root.title("Calculator")

e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#e.insert(0,"")

def btn_click(num):
    #return
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))
    
def btn_clear():
    e.delete(0,END)

def btn_add():
    first_no = e.get()
    global fn
    global math
    math= "Addition"
    fn = int(first_no)
    e.delete(0,END)

def btn_sub():
    first_no = e.get()
    global fn
    global math
    math= "Subtraction"
    fn = int(first_no)
    e.delete(0,END)

def btn_mul():
    first_no = e.get()
    global fn
    global math
    math= "Multiplication"
    fn = int(first_no)
    e.delete(0,END)

def btn_div():
    first_no = e.get()
    global fn
    global math
    math= "Division"
    fn = int(first_no)
    e.delete(0,END)    
   
def btn_equal():
    sec_no = e.get()
    e.delete(0,END)
    
    if math== "Addition":
        e.insert(0,fn + int(sec_no))
    if math== "Subtraction":
        e.insert(0,fn - int(sec_no))
    if math== "Multiplication":
        e.insert(0,fn * int(sec_no))
    if math== "Division":
        e.insert(0,fn / int(sec_no))
   
#define butttons 
btn1=Button(root,text="1",padx=40,pady=20,command=lambda: btn_click(1))
btn2=Button(root,text="2",padx=40,pady=20,command=lambda: btn_click(2))
btn3=Button(root,text="3",padx=40,pady=20,command=lambda: btn_click(3))
btn4=Button(root,text="4",padx=40,pady=20,command=lambda: btn_click(4))
btn5=Button(root,text="5",padx=40,pady=20,command=lambda: btn_click(5))
btn6=Button(root,text="6",padx=40,pady=20,command=lambda: btn_click(6))
btn7=Button(root,text="7",padx=40,pady=20,command=lambda: btn_click(7))
btn8=Button(root,text="8",padx=40,pady=20,command=lambda: btn_click(8))
btn9=Button(root,text="9",padx=40,pady=20,command=lambda: btn_click(9))
btn0=Button(root,text="0",padx=40,pady=20,command=lambda: btn_click(0))

btnadd=Button(root,text="+",padx=40,pady=20,command=btn_add)
btnsub=Button(root,text="-",padx=40,pady=20,command=btn_sub)
btnmul=Button(root,text="*",padx=40,pady=20,command=btn_mul)
btndiv=Button(root,text="/",padx=40,pady=20,command=btn_div)

btnequal=Button(root,text="=",padx=40,pady=20,command=btn_equal)
btnclear=Button(root,text="C",padx=40,pady=20,command=lambda: btn_clear())

#put the buttons on the screen
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=0)
btnequal.grid(row=4,column=1)

btnadd.grid(row=4,column=2)
btnsub.grid(row=5,column=0)
btnmul.grid(row=5,column=1)
btndiv.grid(row=5,column=2)



btnclear.grid(row=6,column=0)


root.mainloop()