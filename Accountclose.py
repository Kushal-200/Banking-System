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
def acco():
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
    win.title(" Ticket Booking")
    win.geometry("800x700+80+50")
    win.config(bg="#7DF9FF")
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    print(mydb)
    def clearfield():
        t2.delete(0, END)
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
        mycur.execute("select max(trno) from accclose")
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
        mycur = mydb.cursor()
        mycur.execute("insert into accclose values("+s1+",'"+s2+"',"+s3+",'" +s4+ "',"+s5+")")
        mydb.commit()
        #mycur.execute("update applicant set cf='Y' where ano="+s3)
        #mydb.commit()

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
        amt=amt-int(s5)
        print(amt)
        mydb.commit()
        mycur = mydb.cursor()
        mycur.execute("update final set ramount="+str(amt)+" where ano="+str(s3))
        mydb.commit()
        lname.config(text="")

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
        mycur = mydb.cursor()
        mycur.execute("select ramount from final where ano=" + str(msno))
        data1 = mycur.fetchone()
        t5.insert(0,data1)
    def serrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        mycur=mydb.cursor()
        s1=t1.get()
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        mycur.execute("select * from accclose where trno="+str(s1))
        data=mycur.fetchone()
        print(data)
        if data is None:
            messagebox.showinfo("WARNING..!","Record is not found")
        else:
            t2.insert(0, data[1])
            t3.insert(0, data[2])
            t4.insert(0, data[3])
            t5.insert(0, data[4])
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

            #t6.insert(0, data[5])

        #else:
            #t3.insert(0,data[2])
            #t4.insert(0,data[3])
           # t5.insert(0,data[4])

    def delrec():
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bank"
            )
        s1=t3.get()
        res=messagebox.askyesno("CONFIRM","Are you sure..?")
        if res==1:
            mycur=mydb.cursor()
            mycur.execute("delete from applicant where ano="+str(s1))
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is deleted..!")
            t1.delete(0,END)
            clearfield()
    ##Label Name##

    l1=Label(win,text="  ACCOUNT CLOSE  ",font=("cooper Black",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l1.place(x=250,y=20)
    lname = Label(win, relief=RIDGE ,borderwidth=1,fg='white',bg='black', font=("arial", 16))
    lname.place(x=350, y=280)
    l2=Label(win,text=" Trno :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l2.place(x=50,y=80)
    l3=Label(win,text=" Trdate :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l3.place(x=50,y=160)
    l4=Label(win,text=" Ano :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l4.place(x=50,y=240)
    l5=Label(win,text=" Reason :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l5.place(x=50,y=320)
    l6=Label(win,text=" Return Amount :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l6.place(x=50,y=400)
    l7=Label(win,text=" Name :- ",font=("arial",16),relief=RIDGE ,borderwidth=1,fg='white',bg='black')
    l7.place(x=250,y=280)
    ###Text Name###
    t1=Entry(win,bd=2,font=("arial",15))
    t1.place(x=250,y=80)
    text = datetime.date.today()
    t2=Entry(win,bd=2,font=("arial",15))
    t2.place(x=250,y=160)
    t2.insert(0,text)
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
    t3.place(x=250,y=240)
    t3.bind("<<ComboboxSelected>>",abc)
    t4=Entry(win,bd=2,font=("arial",15))
    t4.place(x=250,y=320)
    t5=Entry(win,bd=2,font=("arial",15))
    t5.place(x=250,y=400)

    ###Button Name###`
    b1=Button(win,text="ADD",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black',command=addrec)
    b1.place(x=70,y=480)
    b2=Button(win,text="SAVE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black',command=saverec)
    b2.place(x=170,y=480)
    b3=Button(win,text="SEARCH",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black',command=serrec)
    b3.place(x=280,y=480)
    b4=Button(win,text="UPDATE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black')
    b4.place(x=90,y=560)
    b5=Button(win,text="DELETE",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black',command=delrec)
    b5.place(x=220,y=560)
    b6=Button(win,text="EXIT",font=("arial",15,"bold"),relief=RIDGE ,borderwidth=10,fg='white',bg='black')
    b6.place(x=350,y=560)
    win.mainloop()
#acco()



