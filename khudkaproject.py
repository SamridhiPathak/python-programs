import sqlite3
from tkinter import *
from tkinter import messagebox
class DB:
    def __init__(self):
        self.con=sqlite3.connect("yourbook.db")
        self.cursor=self.con.cursor()
        self.con.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,price INTEGER)")
        
        self.con.commit()

    def __del__(self): #This is Distructor
        self.con.close() #close connection

    
#Get All Books
    def books(self):
        self.cursor.execute("SELECT * FROM book")
        rows=self.cursor.fetchall() #get All Rows from database
        return rows
#Insert Data
    def insert(self,book_name,price):
        self.cursor.execute("INSERT INTO books VALUES(NULL,?,?)",(book_name,isbn))
        self.con.commit()
#Search Into DATABASE
    def search(self,book_name="",price=""):
        self.cursor.execute("SELECT * FROM books WHERE book_namae=?OR price=?", (title,price))
        found_rows=self.cursor.fetchall()
        return found_rows

db=DB()
    
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

def search_command():
    list1.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),isbn_text.get()):
        
        list1.insert(END,row)
window=Tk()
window.title("Book  Form")

def on_closing():
    dd=db
    
    if messagebox.askokcancel("Exit","Are you sure?"):
        window.destroy()
        del dd #DB destructor

window.protocol("WM_DELETE_WINDOW",on_closing)


l1=Label(window,text="BOOK_NAME")
l1.grid(row=0,column=0)

l3=Label(window,text="PRICE")
l3.grid(row=1,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

isbn_text=StringVar()
e3=Entry(window,textvariable=isbn_text)
e3.grid(row=1,column=1)

list1=Listbox(window,height=6,width=55)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

window.mainloop()



































