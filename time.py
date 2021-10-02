from tkinter import *
#from PIL import ImageTk,Image
import sqlite3
root=Tk()
root.title("Time Calculation")
root.geometry("300x200")


#==========================================================================
#create LABELS
lblft= Label(root,text="First time :")
lblft.grid(row=0,column=0,pady=10)

lblst= Label(root,text="Second time :")
lblst.grid(row=1,column=0,pady=10)

lbltt= Label(root,text="Third time :")
lbltt.grid(row=2,column=0,pady=10)
#==========================================================================
#create Labels
txth1= Entry(root,width=10)
txth1.grid(row=0,column=1)

txtm1= Entry(root,width=10)
txtm1.grid(row=0,column=2)

txts1= Entry(root,width=10)
txts1.grid(row=0,column=3)

txth2= Entry(root,width=10)
txth2.grid(row=1,column=1)

txtm2= Entry(root,width=10)
txtm2.grid(row=1,column=2)

txts2= Entry(root,width=10)
txts2.grid(row=1,column=3)

txth3= Entry(root,width=10)
txth3.grid(row=2,column=1)

txtm3= Entry(root,width=10)
txtm3.grid(row=2,column=2)

txts3= Entry(root,width=10)
txts3.grid(row=2,column=3)
#==========================================================================
def Solve():
    flag = 0
    h1= int(txth1.get())
    m1= int(txtm1.get())
    s1= int(txts1.get())
    h2= int(txth2.get())
    m2= int(txtm2.get())
    s2= int(txts2.get())
    
    if s2 > s1 :
        s1 += 60
        m1 -= 1
        
    if m2 > m1 :
        m1 += 60
        h1 -= 1
    
    if h2 > h1 :
        txth3.insert(0,str("plz"))
        flag = 1
         
    if flag == 1 :
        #txth3.insert(0,int(h1) - int(h2))
        txtm3.insert(0,int(m1) - int(m2))
        txts3.insert(0,int(s1) - int(s2))
    else :
        txth3.insert(0,int(h1) - int(h2))
        txtm3.insert(0,int(m1) - int(m2))
        txts3.insert(0,int(s1) - int(s2))
 
 
 
 
def clear():
    
    
    txth3.delete(0,END)
    txtm3.delete(0,END)
    txts3.delete(0,END)
    

#==========================================================================
#create submit button
submit_button= Button(root,text="Calculate",command=Solve)                                 #insert into table
submit_button.grid(row=3,column=0,columnspan=4,pady=10,padx=10,ipadx=100)

Clear_button= Button(root,text="Clear",command=clear)                                 #insert into table
Clear_button.grid(row=4,column=0,columnspan=4,pady=10,padx=10,ipadx=100)



root.mainloop()


"""
                                                    a= txth1.get()
                                                    b= txth2.get()
                                                    c= int(a) + int (b)
                                                    txth3.insert (0 ,c)
"""

