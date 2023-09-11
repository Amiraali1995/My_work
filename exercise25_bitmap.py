from  tkinter import *

window=Tk()
window.geometry('400x500')
bitmapBtn1=Button(window,text='error',bitmap='error')
bitmapBtn1.pack()

bitmapBtn2=Button(window,text='hourglass',bitmap='hourglass')
bitmapBtn2.pack()

bitmapBtn3=Button(window,text='info',bitmap='info')
bitmapBtn3.pack()

bitmapBtn4=Button(window,text='question',bitmap='question')
bitmapBtn4.pack()

bitmapBtn5=Button(window,text='gray12',bitmap='gray12')
bitmapBtn5.pack()

bitmapBtn7=Button(window,text='gray25',bitmap='gray25')
bitmapBtn7.pack()


window.mainloop()