from tkinter import *
#from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Working with databases")
root.geometry("400x400")





conn = sqlite3.connect('mynewdb.db')
c = conn.cursor()





# c.execute(""" CREATE TABLE tbl_addrnew( 
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)
#          """)



#print(c.execute('show tables'))



conn.commit()


conn.close()


#create tables


root.mainloop()
