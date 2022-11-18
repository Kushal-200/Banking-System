from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
     user="root",
     password="",
     database="bank"
 )

print(mydb)
def wit():
    win = Toplevel()
    win.attributes('-fullscreen', True)
    path = Image.open("image4.png")
    render = ImageTk.PhotoImage(path)
    img = Label(win, image=render)
    img.place(x=0, y=0)
    win.attributes('-fullscreen', True)
    b1 = Button(win, text="Back", command=win.destroy)
    b1.place(x=5, y=5)
    b2 = Button(win, text="Exit", command=quit)
    b2.place(x=50, y=5)

    win.title(" Banking System")
    win.geometry("1000x1000+80+50")
    win.config(bg="#7DF9FF")
    def clearfield():
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)


    def addrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        mycur=mydb.cursor()
        mycur.execute("select max(trno) from withdraw")
        data=mycur.fetchone()
        c=0
        c=data[0]
        c=c+1
        t1.delete(0, END)
        t1.insert(0, c)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
    def saverec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        s1=t1.get()
        dt=datetime.date.today()
        s2=dt.strftime("%Y-%m-%d")
        print(s2)
        s3=t3.get()
        s4=t4.get()
        s5=t5.get() 
        #print(s2)
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
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        mycur = mydb.cursor()
        mycur.execute("select ramount from final where ano="+str(s3))
        bal = mycur.fetchone()
        balance=str(bal[0])
        wbal=str(s5)
        print(balance,wbal)
        if balance > wbal:
            mycur = mydb.cursor()
            mycur.execute("insert into withdraw values("+s1+",'"+s2+"',"+s3+",'" +s4+ "',"+s5+")")
            mydb.commit()
            messagebox.showinfo("CONFIRM", "Record is saved..!")
            mycur = mydb.cursor()
            mycur.execute("select ramount from final where ano=" + str(s3))
            amt = mycur.fetchone()
            print(amt[0], s5)
            amt = int(amt[0])
            amt = amt - int(s5)
            print(amt)
            mydb.commit()
            mycur = mydb.cursor()
            mycur.execute("update final set ramount=" + str(amt) + " where ano=" + str(s3))
            mydb.commit()
            lname.config(text="")
        else:
            messagebox.showinfo("CONFIRM", "INSUFICIENT BALANCE")
        t1.delete(0, END)
        clearfield()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )

    lname = Label(win, fg='black', bg="#7DF9FF", font=("arial", 16))
    lname.place(x=600, y=240)


    def abc(end, s1=None):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        mycur = mydb.cursor()
        mycur.execute("select apname from applicant where ano="+str(s1))
        data = mycur.fetchall()
        print(data)


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

        mycur.execute("select * from withdraw where trno="+str(s1))
        data=mycur.fetchone()
        #date=int(data[1])
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
            mycur.execute("delete from withdraw where trno="+str(s1))
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is deleted..!")
            t1.delete(0,END)
            clearfield()




    l1=Label(win,text="  WITHDRAW FORM ",font=("cooper Black",20),borderwidth=2,fg="white",bg='black',relief="solid")
    l1.place(x=400,y=20)
    l2=Label(win,text=" Trno :- ",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l2.place(x=50,y=80)
    l3=Label(win,text=" Trdate :- ",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l3.place(x=50,y=160)
    l4=Label(win,text=" Apno :-",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l4.place(x=50,y=240)
    l5=Label(win,text=" perticular :- ",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l5.place(x=50,y=320)
    l6=Label(win,text=" Amount :- ",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l6.place(x=50,y=400)
    l7=Label(win,text=" Name :-",font=("arial",16),borderwidth=5,fg="white",bg='black')
    l7.place(x=530,y=240)


    t1=Entry(win,bd=2,font=("arial",15))
    t1.place(x=250,y=80)
    date=datetime.date.today()
    t2=Entry(win,bd=2,font=("arial",15))
    t2.place(x=250,y=160)
    t2.insert(0, date)
    #t3=Entry(win,bd=2,font=("arial",15))
    #t3.place(x=250,y=240)
    #t4=Entry(win,bd=2,font=("arial",15))
    #t4.place(x=250,y=320)
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

    #mydb.commit()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    mycur = mydb.cursor()
    mycur.execute("select ano from applicant" )
    val=mycur.fetchall()
    value=[]
    #print(val)
    for i in val:
        if i not in data1:
            value.append(i)
            print(i)
    t3 = Combobox(win, values=value, font=("arial", 15))
    t3.place(x=250,y=240)
    t3.bind("<<ComboboxSelected>>",abc)
    per=("By Cash","By Cheque","By DD")
    t4=Combobox(win,values=per,font=("arial",15))
    t4.place(x=250,y=320)

    t5=Entry(win,bd=2,font=("arial",15))
    t5.place(x=250,y=400)

    b1=Button(win,text="ADD",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=addrec)
    b1.place(x=50,y=500)
    b2=Button(win,text="SAVE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=saverec)
    b2.place(x=150,y=500)
    b3=Button(win,text="SEARCH",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=serrec)
    b3.place(x=250,y=500)
    #b4=Button(win,text="UPDATE",font=("arial",16),borderwidth=2,relief="solid")
    #b4.place(x=370,y=500)
    b5=Button(win,text="DELETE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=delrec)
    b5.place(x=400,y=500)
    b6=Button(win,text="EXIT",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=quit)
    b6.place(x=520,y=500)
    #cd=Label(win,text=datetime.date.today(),bg="#7DF9FF",font=("arial",14))
    #cd.place(x=800,y=30)
    win.mainloop()

#wit()
