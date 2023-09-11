# Import the tkinter library
from tkinter import *

# Create the main window
window = Tk()

# Set the dimensions of the main window
window.geometry('500x500')
window.configure(bg='lightgray')  # Set the background color to light gray

# Create buttons with different cursor styles and labels
btn1 = Button(window, text='Circle', cursor='circle', width=30)
btn1.pack()

btn2 = Button(window, text='Cross', cursor='cross', width=30)
btn2.pack()

btn3 = Button(window, text='Plus', cursor='plus', width=30)
btn3.pack()

btn4 = Button(window, text='Mouse', cursor='mouse', width=30)
btn4.pack()

btn5 = Button(window, text='Clock', cursor='clock', width=30)
btn5.pack()

btn6 = Button(window, text='Heart', cursor='heart', width=30)
btn6.pack()

btn7 = Button(window, text='Spider', cursor='spider', width=30)
btn7.pack()

btn7 = Button(window, text='Sizing', cursor='sizing', width=30)
btn7.pack()

btn8 = Button(window, text='Trek', cursor='trek', width=30)
btn8.pack()

btn9 = Button(window, text='Target', cursor='target', width=30)
btn9.pack()

# Create a label with a cursor style
label = Label(window, text='Cursor Course', cursor='man')
label.pack()

# Start the GUI application's main event loop
window.mainloop()
