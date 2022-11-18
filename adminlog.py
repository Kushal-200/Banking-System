from tkinter import*
from tkinter import messagebox
import datetime

#import logingpage
import mysql.connector
#def main():
win=Tk()
win.attributes('-fullscreen',True)

b1 = Button(win, text="Back", command=win.destroy)
b1.place(x=5, y=5)
b2 = Button(win, text="Exit", command=quit)
b2.place(x=50, y=5)
win.title("MAIN FORM")
win.config(bg="#3289a8")

def login():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    s1 = t1.get()
    s2 = t2.get()
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant")
    aname = mycur.fetchall()
    print(aname)

    mycur = mydb.cursor()
    mycur.execute("select ano from applicant")
    ano = mycur.fetchall()
    print(ano)

    if s1 == "":
        messagebox.showwarning("WARNING..!", "Please enter USERNAME")
        return
    if s1 == "Hemant" and s2 == "12345":
        messagebox.showinfo("Message..", "Login Successfully")
        t1.delete(0, END)
        t2.delete(0, END)
        def hello():
            import info
        hello()
        mydb.commit()
        #mainwin.distroy()
    else:
        messagebox.showinfo("Message..", "Wrong id or pass")

    if s2 == "":
        messagebox.showwarning("WARNING..!", "Please enter PASSWORD")
        return
    mycur = mydb.cursor()




l2=Label(win,text=" Bank Of Spain  ",font=("Berlin sans Fb",80),fg='white',bg="#3289a8")
l2.place(x=450,y=40)
l1 = Label(win, text="Professor loging", font=("cooper Black", 35), fg='#595959', bg="#3289a8")
l1.place(x=850, y=250)
t2 = Label(win, text=datetime.date.today(), bd=2, font=("arial", 20), bg="#3289a8")
t2.place(x=1300, y=20)
l2 = Label(win, text=" USERNAME ", font=("arial", 22, "bold"), bg='#3289a8')
l2.place(x=800, y=350)
l3 = Label(win, text=" PASSWORD ", font=("arial", 22, "bold"), bg='#3289a8')
l3.place(x=800, y=400)
t1 = Entry(win, bd=2, font=("arial", 15))
t1.place(x=1010, y=350)
t2 = Entry(win, bd=2, font=("arial", 15))
t2.place(x=1010, y=400)
b1 = Button(win, text="    LOG    ", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=12, fg='white',bg='#3289a8',command=login)
b1.place(x=900, y=450)
b2 = Button(win, text="    Exit    ", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=12, fg='#404040',bg='#3289a8', command=win.destroy)
b2.place(x=1050, y=450)

win.mainloop()
#main()
