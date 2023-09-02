from tkinter import *
from tkinter import ttk

window=Tk()

window.geometry('600x400')

combo1=ttk.Combobox(window,state='readonly',width=30,
  values=('Female','Male','Other'))
combo1.place(x=1,y=1)

combo2=ttk.Combobox(window,state='readonly',width=30,
  values=('Oman','Qatar','Sudia','UAE'))
combo2.place(x=1,y=40)
window.mainloop()