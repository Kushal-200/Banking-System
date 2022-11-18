from tkinter import*
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
def inte():


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
    win.config(bg='#7DF9FF')

    def clearfield():
        #t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t7.delete(0, END)



    def addrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        mycur=mydb.cursor()
        mycur.execute("select max(trno) from intcal")
        data=mycur.fetchone()
        c=0
        c=data[0]
        c=c+1
        t1.delete(0, END)
        t1.insert(0, c)
        clearfield()
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
        t6.delete(0,END)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        mycur = mydb.cursor()
        mycur.execute("select ramount from final where ano="+str(msno))
        val = mycur.fetchall()
        mydb.commit()
        t6.insert(0,val)


        #lname.config(text="")
    lname = Label(win, borderwidth=3,fg="white",bg='black', font=("arial", 16))
    lname.place(x=370, y=260)

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
            messagebox.showwarning("WARNING..!","Please enter ano..")
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
            mycur.execute("delete from applicant where apno="+str(s1))
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is deleted..!")
            t1.delete(0,END)
            clearfield()
    def cal():

        date1=t4.get()
        #date1=datetime.date.date1()
        dat1= datetime.datetime.strptime(date1,"%Y-%m-%d").date()
        date2=t5.get()
        #date2=datetime.date.date2()
        dat2= datetime.datetime.strptime(date2,"%Y-%m-%d").date()
        ano=t3.get()
        print(dat1,dat2)
        #datediff=dat2-dat1
        diffm=(dat2.year-dat1.year)*12+(dat2.month-dat1.month)
        print(diffm)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
        )
        mycur = mydb.cursor()
        sql=("select sum(amount) from deposite where trdate between '"+ str(dat1 )+"' and '" +str(dat2)+ "' and ano ="+ano)
        mycur.execute(sql)
        amt = mycur.fetchone()
        amt=amt[0]
        ##
        mycur = mydb.cursor()
        sql = ("select sum(amount) from withdraw where trdate between '" + str(dat1) + "' and '" + str(
            dat2) + "' and ano =" + ano)
        mycur.execute(sql)
        amtw = mycur.fetchone()
        amtw =amtw[0]

        intv=amt-amtw
        print(intv)

        intcal=intv*7*diffm/100
        print(intcal)
        t7.insert(0,intcal)
    l1=Label(win,text="  INTEREST CALCULATOR  ",font=("cooper Black",23),borderwidth=8,fg="white",bg='black')
    l1.place(x=560,y=20)
    l2=Label(win,text=" Trno  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l2.place(x=50,y=80)
    l3=Label(win,text=" Trdate  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l3.place(x=50,y=160)
    l4=Label(win,text=" Apno  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l4.place(x=50,y=215)
    l5=Label(win,text=" Ifrom  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l5.place(x=50,y=320)
    l6=Label(win,text=" Ito  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l6.place(x=50,y=400)
    l6=Label(win,text=" Amount  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l6.place(x=50,y=480)
    l7=Label(win,text=" Tot Interest  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l7.place(x=50,y=560)
    l8=Label(win,text="  Name  :- ",font=("arial",16),borderwidth=3,fg="white",bg='black')
    l8.place(x=270,y=260)


    t1=Entry(win,bd=2,font=("arial",15))
    t1.place(x=250,y=80)
    #t2=Entry(win,bd=2,font=("arial",15))
    #t2.place(x=250,y=160)
    #t3=Entry(win,bd=2,font=("arial",15))
    #t3.place(x=250,y=240)
    t2=Label(win,text=datetime.date.today(),borderwidth=3,fg="white",bg='black',font=("arial",14))
    t2.place(x=250,y=160)
    per=("")
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
    mycur = mydb.cursor()
    mycur.execute("select ano from applicant" )
    val=mycur.fetchall()
    value = []

    for i in val:
        if i not in data1:
                value.append(i)
                print(i)
        mydb.commit()



    t3=Combobox(win,values=value,font=("arial",15))
    t3.place(x=250,y=215)
    t3.bind("<<ComboboxSelected>>",abc)

    t4=Entry(win,bd=2,font=("arial",15))
    t4.place(x=250,y=320)
    t5=Entry(win,bd=2,font=("arial",15))
    t5.place(x=250,y=400)
    #t5=Label(win,text=datetime.date.today(),bd=2,font=("arial",14),bg="#7DF9FF")
    #t5.place(x=250,y=400)
    t6=Entry(win,bd=2,font=("arial",15))
    t6.place(x=250,y=480)
    t7=Entry(win,bd=2,font=("arial",15))
    t7.place(x=250,y=560)


    b1=Button(win,text="ADD",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=addrec)
    b1.place(x=50,y=620)
    b2=Button(win,text="SAVE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=saverec)
    b2.place(x=150,y=620)
    b3=Button(win,text="SEARCH",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black')
    b3.place(x=250,y=620)
    b4=Button(win,text="UPDATE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black')
    b4.place(x=375,y=620)
    b5=Button(win,text="DELETE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=delrec)
    b5.place(x=500,y=620)
    b6=Button(win,text="EXIT",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black')
    b6.place(x=630,y=620)
    b6=Button(win,text="CALCULATE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=3,fg="white",bg='black',command=cal)
    b6.place(x=530,y=540)
    win.mainloop()

#inte()




