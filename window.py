from tkinter import *
from PIL import ImageTk,Image 

root=Tk()
root.title("New window demo")

def open():
   global img 
   top = Toplevel() 
   img= ImageTk.PhotoImage(Image.open("E:/my pics/dipak.jpg"))
   lbl= Label(top,image=img).pack() 
   btn1= Button(top,text= "This is an other",command=top.destroy).pack()
   
   
   

btn= Button(root,text="Go To Second Window",command = open).pack()
   
root.mainloop()