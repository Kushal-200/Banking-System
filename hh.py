from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.attributes('-fullscreen', True)

win.title(" Banking System")
#win.config(bg='#7DF9FF')


l1=Label(win,text="hemant")
l1.place(x=50,y=100)
path = Image.open("image4.png")
render = ImageTk.PhotoImage(path)
img = Label(win, image=render)
img.place(x=0, y=0)
b1=Button(win,text="Back",command=win.destroy)
b1.place(x=5,y=5)
b2=Button(win,text="Exit",command=quit)
b2.place(x=50,y=5)

t11 = Text(win, height=50, width=70)
t11.place(x=500, y=80)

win.mainloop()
#viewuser()


