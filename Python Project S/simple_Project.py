import sqlite3
from tkinter import *
from tkinter import messagebox
class DB:
    def __init__(self):
        self.con=sqlite3.connect("mybooks.db")
        self.cursor=self.con.cursor()
        self.con.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title TEXT,author TEXT,isbn INTEGER)")
        self.con.commit()

    def __del__(self): #This is Distructor
        self.con.close() #close connection

#Get All Books
    def books(self):
        self.cursor.execute("SELECT * FROM BOOKS")
        rows=self.cursor.fetchall() #get All Rows from database
        return rows
#Insert Data
    def insert(self,title,author,isbn):
        self.cursor.execute("INSERT INTO books VALUES(NULL,?,?,?)",(title,author,isbn))
        self.con.commit()
#Search Into DATABASE
    def search(self,title="",author="",isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR isbn=?", (title,author,isbn))
        found_rows=self.cursor.fetchall()
        return found_rows
#Update data
    def update(self,id,title,author,isbn):
        self.cursor.execute("UPDATE books SET title=?,author=?,isbn=? where id=?",(title,author,isbn,id))
#Delete From Database
    def delete(self,id):
        #print(id)
        self.cursor.execute("DELETE FROM books where id=?",(id,))
        self.con.commit()


db=DB()  #Instantiate Our DB Class

    
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

def view_command():
    list1.delete(0,END)
    for row in db.books():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),isbn_text.get()):
        
        list1.insert(END,row)


def add_command():
    db.insert(title_text.get(),author_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),isbn_text.get()))


def update_command():
    db.update(selected_tuple[0],title_text.get(),author_text.get(),isbn_text.get())
    

def delete_command():
    db.delete(selected_tuple[0])

    
window=Tk()
window.title("Book  Form")

def on_closing():
    dd=db
    
    if messagebox.askokcancel("Exit","Are you sure?"):
        window.destroy()
        del dd #DB destructor

window.protocol("WM_DELETE_WINDOW",on_closing)

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="ISBN")
l3.grid(row=1,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

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

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
