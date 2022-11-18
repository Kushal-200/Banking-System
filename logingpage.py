from tkinter import*
from tkinter import messagebox

from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import mysql.connector


win=Tk()

#
win.attributes('-fullscreen',True)
path = Image.open("image.png")
render1 = ImageTk.PhotoImage(path)
img = Label(win, image=render1)
img.place(x=0, y=0)
# """"""
b1=Button(win,text="Back",command=win.destroy)
b1.place(x=5,y=5)
b2=Button(win,text="Exit",command=quit)
b2.place(x=50,y=5)
win.title(" Banking System")
#win.config(bg='#7DF9FF')
def adminlog():
    import adminlog
    win.distroy()
def login():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    s1 = t1.get()
    s2 = t2.get()
    #mycur = mydb.cursor()
    #mycur.execute("select apname from applicant")
    #aname = mycur.fetchall()

    #print(aname)

    #mycur = mydb.cursor()
    #mycur.execute("select ano from applicant")
    #ano = mycur.fetchall()
    #print(ano)

    if s1 == "":
        messagebox.showwarning("WARNING..!", "Please enter USERNAME")
        return
    if s1 == "Hemant" and s2 == "12345":
        messagebox.showinfo("Message..", "Login Successfully")
        t1.delete(0, END)
        t2.delete(0, END)
        def hello():
            import mainwin
            mainwin.main1()
        hello()
        mydb.commit()

    else:
        messagebox.showinfo("Message..", "Wrong id or pass")

    if s2 == "":
        messagebox.showwarning("WARNING..!", "Please enter PASSWORD")
        return
    mycur = mydb.cursor()



l1=Label(win,text=" Janta Bank ",font=("Arial Rounded MT Bold",60))
l1.place(x=650,y=30)
l1=Label(win,text="Customer Login",font=("Bookman Old Style",35))
l1.place(x=850,y=250)
l2=Label(win,text=" USERNAME ",font=("Bookman Old Style",22,))
l2.place(x=800,y=350)
l3=Label(win,text=" PASSWORD ",font=("Bookman Old Style",22))
l3.place(x=800,y=400)
t1=Entry(win,bd=2,font=("arial",15))
t1.place(x=1010,y=350)
t2=Entry(win,bd=2,font=("arial",15))
t2.place(x=1010,y=400)
#bb1=PhotoImage(file="login.png")

b1=Button(win,text="Login",font=("Bookman Old Style",0),fg="white",borderwidth=12,command=login,bg="black")
b1.place(x=900,y=450)
b2=Button(win,text="   Exit   ",font=("Bookman Old Style",15) ,borderwidth=12,fg="white",bg="black" ,command=win.destroy)
b2.place(x=1100,y=450)
b3=Button(win,text="  adminlog  ",font=("arial",20,"bold"),relief=RIDGE ,borderwidth=12,fg='#404040',command=adminlog)
b3.place(x=300,y=650)
#b4=Button(win,text="Change password",font=("arial",20,"bold"),relief=RIDGE ,borderwidth=12,fg='#404040',command=login)
#b4.place(x=970,y=540)
b5=Button(win,text="Forgot password ",font=("Bookman Old Style",20),relief=RIDGE ,borderwidth=12,fg='#404040',command=win.destroy)
b5.place(x=970,y=550)
mainloop()