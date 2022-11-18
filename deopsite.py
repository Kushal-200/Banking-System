from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime
import mysql.connector
from PIL import Image,ImageTk

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)
print(mydb)
def deo():
    win = Toplevel()
    win.attributes('-fullscreen', True)
    path = Image.open("image4.png")
    render = ImageTk.PhotoImage(path)
    img = Label(win, image=render)
    img.place(x=0, y=0)

    b1 = Button(win, text="Back", command=win.destroy)
    b1.place(x=5, y=5)
    b2 = Button(win, text="Exit", command=quit)
    b2.place(x=50, y=5)

    win.title(" Banking System")
    win.geometry("800x600+80+50")
    win.config(bg="#7DF9FF")
    def addrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        mycur=mydb.cursor()
        mycur.execute("select max(trno) from deposite")
        data=mycur.fetchone()
        c=0
        c=data[0]
        c=c+1
        t1.delete(0, END)
        t1.insert(0, c)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)



    def clearfield():
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)

    def abc(end):
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        msno=t3.get()
        mycur=mydb.cursor()
        mycur.execute("select apname from applicant where ano="+str(msno))
        data=mycur.fetchone()
        print(data)
        lname.config(text=data)
        #lname.config(text="")

    def saverec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        s1=t1.get()
        dt = datetime.date.today()
        s2 = dt.strftime("%Y-%m-%d")
        print(s2)
        s3=t3.get()
        s4=t4.get()
        s5=t5.get()
        if s2=="":
            messagebox.showwarning("WARNING..!","Please enter date..")
            return
        if s3=="":
            messagebox.showwarning("WARNING..!","Please enter apno..")
            return
        if s4=="":
            messagebox.showwarning("WARNING..!","Please enter perticular..")
            return
        if s5=="":
            messagebox.showwarning("WARNING..!","Please enter Amount..")
            return
        mycur = mydb.cursor()
        mycur.execute("insert into deposite values("+s1+",'" +s2+ "',"+s3+",'" +s4+ "',"+s5+")")
        mydb.commit()
        messagebox.showinfo("CONFIRM", "Record is saved..!")
        t1.delete(0, END)
        clearfield()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        mycur = mydb.cursor()
        mycur.execute("select ramount from final where ano="+str(s3))
        amt = mycur.fetchone()
        print(amt[0],s5)
        amt=int(amt[0])
        amt=amt+int(s5)
        print(amt)
        mydb.commit()
        mycur = mydb.cursor()
        mycur.execute("update final set ramount="+str(amt)+" where ano="+str(s3))
        mydb.commit()
    def serrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        mycur=mydb.cursor()
        s1=t1.get()
        clearfield()

        mycur.execute("select * from deposite where trno="+str(s1))
        data=mycur.fetchone()
        print(data)
        if data is None:
            messagebox.showinfo("WARNING..!","Record is not found")
        else:
            t2.insert(0,data[1])
            t3.insert(0,data[2])
            t4.insert(0,data[3])
            t5.insert(0,data[4])
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bank"
            )
            msno = data[2]
            mycur = mydb.cursor()
            mycur.execute("select apname from applicant where ano=" + str(msno))
            data = mycur.fetchone()
            # print(data)
            lname.config(text=data)

    def delrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        s1=t1.get()
        res=messagebox.askyesno("CONFIRM","Are you sure..?")
        if res==1:
            mycur=mydb.cursor()
            mycur.execute("delete from deposite where trno="+str(s1))
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is deleted..!")
            t1.delete(0,END)
            clearfield()
    l1=Label(win,text="  DEPOSITE FORM ",font=("cooper Black",20),fg="white",borderwidth=2,relief="solid",bg="black")
    l1.place(x=280,y=20)
    l2=Label(win,text=" Trno :- ",font=("arial",16),fg='white',borderwidth=2,relief="groove",bg="black")
    l2.place(x=50,y=80)
    l3=Label(win,text=" Trdate :- ",font=("arial",16),fg='white',borderwidth=2,relief="groove",bg="black")
    l3.place(x=50,y=160)
    l4=Label(win,text=" Apno :- ",font=("arial",16),fg='white',borderwidth=2,relief="groove",bg="black")
    l4.place(x=50,y=240)
    l5=Label(win,text=" Particular :- ",font=("arial",16),fg='white',borderwidth=2,relief="groove",bg="black")
    l5.place(x=50,y=320)
    l6=Label(win,text=" Amount :- ",font=("arial",16),fg='white',borderwidth=2,relief="groove",bg="black")
    l6.place(x=50,y=400)
    l7=Label(win,text=" Name :- ",font=("arial",16),fg='white',borderwidth=2,bg="black")
    l7.place(x=250,y=280)
    t1=Entry(win,bd=2,font=("arial",15))
    t1.place(x=250,y=80)
    date=datetime.date.today()

    t2=Entry(win,bd=2,font=("arial",14))
    t2.place(x=250,y=160)
    t2.insert(0, date)
    #t2 = Label(win, text=datetime.date.today(), bd=2, font=("arial", 14), bg="#7DF9FF")
    #t2.place(x=250, y=160)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select ano from accclose ")
    data1 = mycur.fetchall()
    print(data1)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select ano from applicant")
    val = mycur.fetchall()
    value = []
    # print(val)
    for i in val:
        if i not in data1:
            value.append(i)
            print(i)
    t3=Combobox(win,values=value,font=("arial",15))
    t3.place(x=250,y=240)
    t3.bind("<<ComboboxSelected>>",abc)
    per=("By Cash","By Cheque","By DD")
    t4=Combobox(win,values=per,font=("arial",15))
    t4.place(x=250,y=320)
    t5=Entry(win,bd=2,font=("arial",15))
    t5.place(x=250,y=400)
    b1=Button(win,text="ADD",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=5,fg="white",bg='black',command=addrec)
    b1.place(x=50,y=500)
    b2=Button(win,text="SAVE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=5,fg='white',bg='black',command=saverec)
    b2.place(x=150,y=500)
    b3=Button(win,text="SEARCH",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=5,fg='white',bg='black',command=serrec)
    b3.place(x=250,y=500)
    b5=Button(win,text="DELETE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=5,fg='white',bg='black',command=delrec)
    b5.place(x=90,y=580)
    b6=Button(win,text="EXIT",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=5,fg='white',bg='black')
    b6.place(x=210,y=580)
    lname=Label(win,fg='white',bg="black",font=("arial",16))
    lname.place(x=350, y=280)
    win.mainloop()

#deo()



