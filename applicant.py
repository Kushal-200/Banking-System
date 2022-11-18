from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector
from PIL import Image,ImageTk

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)
print(mydb)

def appl():
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
        win.geometry("1500x800")
        win.config(bg='#7DF9FF')

        def clearfield():
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t8.delete(0,END)
            t9.delete(0,END)
            t10.delete(0,END)

        def addrec():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bank"
                )
            mycur=mydb.cursor()
            mycur.execute("select max(ano) from applicant")
            data=mycur.fetchone()
            c=0
            c=data[0]
            c=c+1
            t1.delete(0,END)
            t1.insert(0,c)
            clearfield()

        def saverec():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bank"
                )
            s1=t1.get()
            s2=t2.get()
            s3=t3.get()
            s4=t4.get()
            s5=t5.get()
            s6=t6.get()
            s7=t7.get()
            s8=t8.get()
            s9=t9.get()
            s10=t10.get()
            if s2=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's name..")
                return
            if s3=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's address..")
                return
            if s4=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's city..")
                return
            if s5=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's contact..")
                return
            if s6=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's gender..")
                return
            if s7=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's birth date..")
                return
            if s8=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's age..")
                return
            if s9=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's nominee..")
                return
            if s10=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's opening balance..")
                return
            mycur=mydb.cursor()
            mycur.execute("insert into applicant values("+s1+",'"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+s6+"','"+s7+"','"+s8+"','"+s9+"','"+s10+"','N')")
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is saved..!")
            t1.delete(0,END)
            clearfield()
            mycur = mydb.cursor()
            mycur.execute("insert into final values(" + s1 + "," + s10 + ")")
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
            mycur.execute("select * from applicant where ano="+str(s1))
            data=mycur.fetchone()
            if data is None:
                messagebox.showinfo("WARNING..!","Record is not found")
            else:
                t2.insert(0,data[1])
                t3.insert(0,data[2])
                t4.insert(0,data[3])
                t5.insert(0,data[4])
                t6.insert(0,data[5])
                t7.insert(0,data[6])
                t8.insert(0,data[7])
                t9.insert(0,data[8])
                t10.insert(0,data[9])
                #clrtext()
                da="\n All Record"
                da=da + "\n\n Account no  :" +str(data[0])
                da=da + "\n Name          :" +str(data[1])
                da =da + "\n Addaress     :" + str(data[2])
                da =da + "\n city         :" + str(data[3])
                da =da + "\n contact      :" + str(data[4])
                da =da + "\n Gender       :" + str(data[5])
                da =da + "\n Birthdate   :" + str(data[6])
                da =da + "\n Age          :" + str(data[7])
                da =da + "\n Nominee      :" + str(data[8])
                da =da + "\n Balance      :" + str(data[9])
                t11.delete('1.0',END)
                t11.insert(END,da)

        def uprec():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bank"
                )
            s1=t1.get()
            s2=t2.get()
            s3=t3.get()
            s4=t4.get()
            s5=t5.get()
            s6=t6.get()
            s7=t7.get()
            s8=t8.get()
            s9=t9.get()
            s10=t10.get()

            if s2=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's name..")
                return
            if s3=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's address..")
                return
            if s4=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's city..")
                return
            if s5=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's contact..")
                return
            if s6=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's gender..")
                return
            if s7=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's birth date..")
                return
            if s8=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's age..")
                return
            if s9=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's nominee..")
                return
            if s10=="":
                messagebox.showwarning("WARNING..!","Please enter applicant's opening balance..")
                return
            mycur=mydb.cursor()
            mycur.execute("update applicant set apname='"+s2+"',address='"+s3+"',city='"+s4+"',contact='"+s5+"',gender='"+s6+"',bdate='"+s7+"',age='"+s8+"',nomine='"+s9+"',opbalnce='"+s10+"' where ano="+s1)
            mydb.commit()
            messagebox.showinfo("CONFIRM","Record is updated")
            t1.delete(0,END)
            clearfield()


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
                mycur.execute("delete from applicant where ano="+str(s1))
                mydb.commit()
                messagebox.showinfo("CONFIRM","Record is deleted..!")
                t1.delete(0,END)
                clearfield()


        l1=Label(win,text="  CUSTOMER INFORMATION  ",font=("cooper Black",20),fg='white',borderwidth=2,bg="black",relief="groove")
        l1.place(x=400,y=20)
        l2=Label(win,text=" Application no :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l2.place(x=50,y=80)
        l3=Label(win,text=" Appicant Name :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l3.place(x=50,y=160)
        l4=Label(win,text=" Address :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l4.place(x=50,y=240)
        l5=Label(win,text=" City :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l5.place(x=50,y=320)
        l6=Label(win,text=" Contact :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l6.place(x=50,y=400)

        t1=Entry(win,bd=2,font=("arial",15))
        t1.place(x=250,y=80)
        t2=Entry(win,bd=2,font=("arial",15))
        t2.place(x=250,y=160)
        t3=Entry(win,bd=2,font=("arial",15))
        t3.place(x=250,y=240)
        t4=Entry(win,bd=2,font=("arial",15))
        t4.place(x=250,y=320)
        t5=Entry(win,bd=2,font=("arial",15))
        t5.place(x=250,y=400)
        l7=Label(win,text=" Gender :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l7.place(x=550,y=80)
        l8=Label(win,text=" Birth Date :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l8.place(x=550,y=160)
        l9=Label(win,text=" Age :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l9.place(x=550,y=240)
        l10=Label(win,text=" Nomine :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l10.place(x=550,y=320)
        l11=Label(win,text=" opening Balance :- ",font=("arial",16),fg='white',borderwidth=2,bg="black",relief="groove")
        l11.place(x=550,y=400)

        #t6=Entry(win,bd=2,font=("arial",15))
        #t6.place(x=750,y=80)
        per=("Male","Female","Other")
        t6=Combobox(win,values=per,font=("arial",15))
        t6.place(x=750,y=80)
        t7=Entry(win,bd=2,font=("arial",15))
        t7.place(x=750,y=160)
        t8=Entry(win,bd=2,font=("arial",15))
        t8.place(x=750,y=240)
        t9=Entry(win,bd=2,font=("arial",15))
        t9.place(x=750,y=320)
        t10=Entry(win,bd=2,font=("arial",15))
        t10.place(x=750,y=400)
        t11=Text(win,height=22,width=60)
        t11.place(x=1000,y=80)
        b1=Button(win,text="ADD",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=addrec)
        b1.place(x=50,y=500)
        b2=Button(win,text="SAVE",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=saverec)
        b2.place(x=150,y=500)
        b3=Button(win,text="SEARCH",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=serrec)
        b3.place(x=250,y=500)
        b4=Button(win,text="UPDATE",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=uprec)
        b4.place(x=70,y=580)
        b5=Button(win,text="DELETE",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=delrec)
        b5.place(x=200,y=580)
        b6=Button(win,text="EXIT",font=("arial",15,"bold"),relief=RIDGE ,fg='white',borderwidth=2,bg="black",command=quit)
        b6.place(x=330,y=580)

        win.mainloop()
appl()
