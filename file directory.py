from tkinter import *
from PIL import ImageTk,Image 
from tkinter import filedialog

root=Tk()
root.title("File Dialog box demo")

def open():
    root.filename = filedialog.askopenfilename(initialdir= "D:/dos",title= "Select a file",
     filetypes= (("jpg files","*.jpg"),("all files","*,*"))) 
    lbl= Label(root,text= root.filename).pack()
    img= ImageTk.PhotoImage(Image.open(root.filename))
    lbl2= Label(root,image=img).pack()

btn= Button(root,text="Click Me",command=open).pack()
  
root.mainloop()