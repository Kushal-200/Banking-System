from tkinter import *
#from tkinter.ttk import Combobox
import datetime
import deopsite
import withdraw
import Accountclose
import applicant


import Interestcalculator11

from PIL import Image,ImageTk

def main1():
    win=Toplevel()
    win.attributes('-fullscreen', True)
    path=Image.open("image4.png")
    render =ImageTk.PhotoImage(path)
    img=Label(win,image=render)
    img.place(x=0,y=0)
    b1 = Button(win, text="Back", command=win.destroy)
    b1.place(x=5, y=5)
    b2 = Button(win, text="Exit", command=quit)
    b2.place(x=50, y=5)
    win.title("MAIN FORM")
    #win.config(bg="#7DF9FF")
    win.geometry("500x500+100+100")
    l2=Label(win,text=" Janta Bank  ",font=("Berlin sans Fb",80),borderwidth=3,relief="groove",fg='White',bg="black")
    l2.place(x=450,y=40)
    l2=Label(win,text="  MAIN FORM  ",font=("arial",25),fg='white',borderwidth=3,relief="groove",bg="black")
    l2.place(x=650,y=300)
    t2 = Label(win, text=datetime.date.today(),fg='white',borderwidth=3,relief="groove",bg="black", font=("arial", 20))
    t2.place(x=1300, y=20)
    b1=Button(win,text="     Applicant     ",font=("arial",22),fg='white',borderwidth=3,relief="groove",command=applicant.appl,bg="black")
    b1.place(x=500,y=400)
    b2=Button(win,text="      Deposite    ",font=("arial",22),fg='white',borderwidth=3,relief="groove",command=deopsite.deo,bg="black")
    b2.place(x=500,y=500)
    b3=Button(win,text="    Withdraw     ",font=("arial",22),fg='white',borderwidth=3,relief="groove",command=withdraw.wit,bg="black")
    b3.place(x=500,y=600)
    b4=Button(win,text="       Int cal        ",font=("arial",22),fg='white',borderwidth=3,relief="groove",bg="black",command=Interestcalculator11.inte)
    b4.place(x=800,y=400)
    b5=Button(win,text="Account close  ",font=("arial",22),fg='white',borderwidth=3,relief="groove",bg="black",command=Accountclose.acco)
    b5.place(x=800,y=500)
    b6=Button(win,text="        Exit           ",font=("arial",22),fg='White',borderwidth=3,relief="groove",bg="black",command=win.destroy)
    b6.place(x=800,y=600)
    win.mainloop()
main1()