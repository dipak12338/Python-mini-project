from tkinter import *
#from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Working with databases")
root.geometry("400x400")



#create tables
'''
c.execute(""" CREATE TABLE addresses( 
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)
         """)
'''
# create submit function

def submit():
    #Databse
    con= sqlite3.connect('address_book.db')
    # Create cursor
    c = con.cursor()
    #inserting 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city , :state , :zipcode)",
              {
              'f_name' : f_name.get(),
              'l_name': l_name.get(),
              'address': address.get(),
              'city': city.get(),
              'state': state.get(),
              'zipcode': zipcode.get()   
              }
             )
    #commit changes
    con.commit()
    #close connection
    con.close()
    
    f_name.delete(0,END)
    l_name.delete(0,END)
    state.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    
    
#create query function
def  query():
    #Databse
    con= sqlite3.connect('address_book.db')
    # Create cursor
    c = con.cursor()
    
    #query the databasesss
    
    c.execute("Select *, oid from addresses")
    rec = c.fetchall()                #fetchone fetchmany()
    print(rec)
    
    print_rec= "" 
    for r in rec:
        print_rec += str(r[0]) + " " + str(r[1]) +   " " +  "\t" +   str(r[6])  + "\n" 
        
    qlbl= Label(root,text=print_rec)
    qlbl.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

    
    
    #commit changes
    con.commit()
    #close connection
    con.close()
 
    
def delete():
    #Databse
    con= sqlite3.connect('address_book.db')
    # Create cursor
    c = con.cursor()
    
    #Delete the reccords
    c.execute("Delete from addresses Where oid= " + delete_box.get())
    #commit changes
    con.commit()
    #close connection
    con.close()
 
def edit():
    global editor
    editor=Tk()
    editor.title("Update the records ")
    editor.geometry("300x200")
    
    #Databse
    con= sqlite3.connect('address_book.db')
    # Create cursor
    c = con.cursor()
    
    r_id= delete_box.get()
    
    #query the databasesss
    
    c.execute("Select * from addresses where oid=" + r_id)
    rec = c.fetchall()                #fetchone fetchmany()
    #print(rec)
    #Loop thru records
   
    #create GLOBAL Variable
    global f_name_editor
    global  state_editor
    global zipcode_editor
    global l_name_editor
    global address_editor
    global city_editor

    
        
    #create Labelss
    f_name_editor= Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1)

    l_name_editor= Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor= Entry(editor,width=30)
    address_editor.grid(row=2,column=1)

    city_editor= Entry(editor,width=30)
    city_editor.grid(row=3,column=1)

    state_editor= Entry(editor,width=30)
    state_editor.grid(row=4,column=1)

    zipcode_editor= Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)

   

    #==========================================================================
    #create text boxes 
    f_name_label= Label(editor,text="First name")
    f_name_label.grid(row=0,column=0)

    l_name_label= Label(editor,text="Last name")
    l_name_label.grid(row=1,column=0)

    address_label= Label(editor,text="Address")
    address_label.grid(row=2,column=0)

    city_label= Label(editor,text="City")
    city_label.grid(row=3,column=0)

    state_label= Label(editor,text="State")
    state_label.grid(row=4,column=0)

    zipcode_label= Label(editor,text="zip codes")
    zipcode_label.grid(row=5,column=0)


    for r in rec:
        f_name_editor.insert(0, r[0])
        l_name_editor.insert(0, r[1])
        address_editor.insert(0, r[2])
        city_editor.insert(0, r[3])
        state_editor.insert(0, r[4])
        zipcode_editor.insert(0, r[5])
    
    
    #create a Update button
    edit_button= Button(editor,text="Save Button",command=update)
    edit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

def update():
       
    #Databse
    con= sqlite3.connect('address_book.db')
    # Create cursor
    c = con.cursor()
     
    r_id = delete_box.get()
    
    c.execute("""UPDATE addresses set 
    first_name = :fr,
    last_name = :ln,
    address = :ad,
    city = :c,
    state = :s,
    zipcode = :zp     
    where oid = :oid""",
    {
    'fr' : f_name_editor.get(),
    'ln' : l_name_editor.get(),
    'ad' : address_editor.get(),
    'c' : city_editor.get(),
    's' : state_editor.get(),
    'zp' : zipcode_editor.get(),
    'oid' : r_id   
    })
    
    

    #commit changes
    con.commit()
    #close connection
    con.close()
    
    
    
    
    
    editor.destroy()
    
    

#create Labels
f_name= Entry(root,width=30)
f_name.grid(row=0,column=1)

l_name= Entry(root,width=30)
l_name.grid(row=1,column=1)

address= Entry(root,width=30)
address.grid(row=2,column=1)

city= Entry(root,width=30)
city.grid(row=3,column=1)

state= Entry(root,width=30)
state.grid(row=4,column=1)

zipcode= Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box= Entry(root,width=30)
delete_box.grid(row=9,column=1)


#==========================================================================
#create text boxes 
f_name_label= Label(root,text="First name")
f_name_label.grid(row=0,column=0)

l_name_label= Label(root,text="Last name")
l_name_label.grid(row=1,column=0)

address_label= Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label= Label(root,text="City")
city_label.grid(row=3,column=0)

state_label= Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label= Label(root,text="Zipcode ")
zipcode_label.grid(row=5,column=0)

delete_box_label = Label(root,text="ID Number ")
delete_box_label.grid(row=10,column=0)




#create submit button
submit_button= Button(root,text="Submit",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a query button
query_button= Button(root,text="Show results",command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a query button
delete_button= Button(root,text="Delete record",command=delete)
delete_button.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a Update button
edit_button= Button(root,text="Update record",command=edit)
edit_button.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=100)







root.mainloop()
