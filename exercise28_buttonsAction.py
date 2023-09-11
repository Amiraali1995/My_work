# Import the tkinter library
from tkinter import *

# Create a main window
window = Tk()

# Set the dimensions of the main window
window.geometry('300x300')

# Create Button 1 with default appearance
btn1 = Button(window, text='Button1')
btn1.pack()

# Create Button 2 with custom active background and foreground colors
btn2 = Button(window, text='Button2', activebackground='black', activeforeground='white')
btn2.pack()

# Create Button 3 with multi-line code for readability
btn3 = Button(window, text='Button3',
              activebackground='red',
              activeforeground='white')
btn3.pack()

# Start the main event loop to display the window
window.mainloop()
