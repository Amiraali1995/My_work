# Import the tkinter library
from tkinter import *

# Create the main window
window = Tk()

# Set the dimensions of the main window
window.geometry('500x500')

# Load an image from a file ('111.png')
photo = PhotoImage(file='111.png')

# Create a label widget with text and an image, with the image positioned on top
imgLabel = Label(window, text='Learn Python Tkinter  ', image=photo, compound=TOP)

# Pack the label widget into the main window
imgLabel.pack()

# Start the GUI application's main event loop
window.mainloop()
