from tkinter import *
from tkinter import messagebox

top = Tk()
def fun():  
    messagebox.showinfo("your form has been submitted")  
  
top.geometry("400x250")
#parent=Tk()
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)
submit=Button(top, text = "Submit", fg= "blue", bg="yellow",bd= "2px black" ,relief="sunken",command= fun).place(x=30, y=180)
e1 = Entry(top).place(x=80, y=50)  
e2 = Entry(top).place(x=80, y=90)  
e3 = Entry(top).place(x=95, y=130)  
top.mainloop()  
