from tkinter import *
import mysql.connector
from tkinter.ttk import Combobox

def viewuser():
    import viewuser
win=Tk()
win.attributes('-fullscreen',True)
b1=Button(win,text="Back",command=win.destroy)
b1.place(x=5,y=5)
b2=Button(win,text="Exit",command=quit)
b2.place(x=50,y=5)
win.title(" Banking System ")
win.config(bg='#7DF9FF')
l1=Label(win,text=" Royal Bank ",font=("Britannic Bold",60),fg='#595959',bg="#7DF9FF")
l1.place(x=500,y=30)
b1=Button(win,text="     View user     ",font=("arial",40,"bold"),relief=RIDGE ,borderwidth=12,fg='#404040',bg='#7DF9FF',command=viewuser)
b1.place(x=300,y=250)
b2=Button(win,text="     Add User     ",font=("arial",40,"bold"),relief=RIDGE ,borderwidth=12,fg='#404040',bg='#7DF9FF')
b2.place(x=470,y=400)
b2=Button(win,text="     Delete user    ",font=("arial",40,"bold"),relief=RIDGE ,borderwidth=12,fg='#404040',bg='#7DF9FF')
b2.place(x=650,y=550)
#mainloop()
