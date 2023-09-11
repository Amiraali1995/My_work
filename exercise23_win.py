# Import the tkinter library
from tkinter import *

# Create the main window
window = Tk()

# Set the dimensions of the main window
window.geometry('400x400')

# Define a function 'window1' for creating a new window
def window1():
    # Create a new window (window1)
    window1 = Tk()
    window1.geometry('200x200')

    # Create a button in the new window to exit it
    btn = Button(window1, text='Exit', command=quit)
    btn.pack()

    # Start the GUI application's main event loop for the new window (window1)
    window1.mainloop()

# Create a button in the main window to trigger the 'window1' function
btn = Button(window, text='My program', command=window1)
btn.pack()

# Start the GUI application's main event loop for the main window
window.mainloop()
