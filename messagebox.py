from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Messagebox in python")

# showinfo  , showwaning ,   showerror    askquesion askokcancel  askyesno   

def popup():
    res = messagebox.askquestion("This is my popup ","Hello world!!!")
    Label(root,text=res).pack()
    if res== "yes":
     Label(root,text="U clicked Yes..").pack()
    else:
     Label(root,text="U clicked No..").pack()
    
    
Button(root,text="Popup",command=popup).pack()

root.mainloop()
============================================
>>> from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> def Myfun():
...   messagebox.showinfo("Message","Hello Friend")
...
>>> b= Button(root,text="Hit me",command=Myfun)
>>> b.pack()
>>> root.geometry("400x400")
''
>>> root.mainloop()