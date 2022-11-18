from tkinter import *
import mysql.connector
win=Tk()
win.attributes('-fullscreen', True)
b1=Button(win,text="Back",command=win.destroy)
b1.place(x=5,y=5)
b2=Button(win,text="Exit",command=quit)
b2.place(x=50,y=5)
win.title(" Banking System")
win.config(bg='#7DF9FF')


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)
def viewuser():
    mycur = mydb.cursor()
    mycur.execute("select * from applicant")
    appli = mycur.fetchall()
    t11.insert(END,appli)


t11 = Text(win, height=28, width=100)
t11.place(x=500, y=80)
viewuser()
win.mainloop()
#viewuser()


