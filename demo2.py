from tkinter import *
root = Tk()

e=Entry(root,width=50,bg="gray")
e.pack()


def myClick():
   lbl= "Hello " + e.get()
   #creating a label
   mylabel = Label(root, text=lbl)
   mylabel.pack()

btn = Button(root, text = "Click Me",command=myClick)
btn.pack()
root.mainloop()
