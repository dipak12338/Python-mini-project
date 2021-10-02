from tkinter import *
#from PIL import ImageTk,Image 

root=Tk()
root.title("Check boxes box demo")
root.geometry("400x400")

def show():
    lbl= Label(root,text=var.get()).pack()
    

var = StringVar()
c = Checkbutton(root,text= "Check this",variable=var,onvalue= "Piizza",offvalue="Burger")     #instead of 0 and 1 we set pizza and burger
c.deselect()
c.pack()
btn= Button(root,text= "Show",command=show).pack()


root.mainloop()
========================================================================================
from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> root.geometry("200x200")
''
>>> c1 = Checkbutton(root,text="option 1").pack()
>>> c2 = Checkbutton(root,text="option 2").pack()
>>> c2 = Checkbutton(root,text="option 2").pack()
>>> c3 = Checkbutton(root,text="option 3").pack()

>>> mainloop()