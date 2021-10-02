from tkinter import *
root=Tk()
root.title("RadioButton in python")

lbl=Entry(root,bg="gray")
lbl.pack()   

topings= [
("A","A"),
("B","B"),
("C","C"),
]
pizza=StringVar()
pizza.set("A")   # otherwise it selects all

for text,x in topings: 
    Radiobutton(root,text=text,variable=pizza,value=x).pack(anchor=W)
    
def clicked():          
    lbl.insert(0,pizza.get())     #it works but in horizontal


btn = Button(root,text="Click Here",command=lambda: clicked())
btn.pack()

root.mainloop()



