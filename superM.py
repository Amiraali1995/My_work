from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

window=Tk()
window.geometry('800x450+280+50')
window.resizable(False,False)
window.title('SUPERMARKET')
window.iconbitmap('C:\\Users\\USER\\Desktop\\python_codes\\SqlSever_GUI_Python\\clogo.ico')
title=Label(window,text='Super Market System',fg='gold',bg='black',font=('tajawal',16,'bold'))
title.pack(fill=X)
url1='https://www.facebook.com'
url2='https://www.linkedin.com/in/amira-al-naamani-2b0818228/'
url3='https://github.com/Amiraali1995'
def open1():
    webbrowser.open_new(url1)

def open2():
    webbrowser.open_new(url2)

def open3():
    webbrowser.open_new(url3)

def about1():
    messagebox.showinfo('Developer','Amira Ali AL-Naamani')

def about2():
    messagebox.showinfo('About the System','SuperMarket Management System on Python Tinter')

window.config(bg='white')
frame1=Frame(window,width=230,height=425,bg='#0B2F3A')
frame1.place(y=30)

Title1=Label(frame1,text='Supermarket project',bg='#0B2F3A',fg='white',font=('tajawal',12,'bold'))
Title1.place(x=42,y=10)

Title2=Label(frame1,text='Developer Amire Ali',bg='#0B2F3A',fg='white',font=('tajawal',12,'bold'))
Title2.place(x=45,y=50)

Title3=Label(frame1,text='Contact us',bg='#0B2F3A',fg='white',font=('tajawal',12,'bold'))
Title3.place(x=47,y=90)

B1=Button(frame1,text='Facebook Account ', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=open1)
B1.place(x=6,y=130)

B2=Button(frame1,text='Linkedin Account  ', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=open2)
B2.place(x=6,y=177)

B3=Button(frame1,text='GitHup Account ', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=open3)
B3.place(x=6,y=225)

B4=Button(frame1,text='About the Developer', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=about1)
B4.place(x=6,y=272)

B5=Button(frame1,text='Project Overview    ', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=about2)
B5.place(x=6,y=318)

B6=Button(frame1,text='Close the Program  ', width=23,fg='black',bg='#DBA901',font=('tajawal',11,'bold'),command=quit)
B6.place(x=6,y=365)

photo=PhotoImage(file='amarket.png')
imo=Label(window,image=photo, bg='white')
imo.place(x=245,y=43,width=450,height=272)

frame2=Frame(window,width=577,height=120,bg='#0B2F3A')
frame2.place(x=229,y=330)

photo1=PhotoImage(file='abc.png')
imo1=Label(window,image=photo1)
imo1.place(x=230,y=338,width=110,height=112)

L1=Label(frame2,text='Username', fg='gold',bg='#0b2f3a',font=('tajawal',12))
L1.place(x=120,y=25)
entery1=Entry(frame2,font=('tajawal',12), justify='center')
entery1.place(x=205, y=26)

L2=Label(frame2,text='Password', fg='gold',bg='#0b2f3a',font=('tajawal',12))
L2.place(x=120,y=70)

entery2=Entry(frame2,font=('tajawal',12), justify='center')
entery2.place(x=205, y=71)

B=Button(frame2,text='Login',bg='#DBA901',font=('tajawal',12),width=12,height=3,fg='black')
B.place(x=420,y=20)


window.mainloop()
