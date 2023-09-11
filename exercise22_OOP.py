from tkinter import *

class TK:
    def __init__(self,window):
        self.window=window
        self.window.geometry('400x400')
        self.window.title('Myprogram')

window=Tk()
ob=TK(window)
window.mainloop()