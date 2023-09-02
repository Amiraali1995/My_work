from tkinter import *
from tkinter import ttk

# Create the main window instance
window = Tk()

# Set the dimensions of the main window
window.geometry('600x400')

# Create RadioButtons for male selection
radiobutton1 = ttk.Radiobutton(window, text='Male1', value=1)
radiobutton1.pack()

radiobutton2 = ttk.Radiobutton(window, text='Male2', value=2)
radiobutton2.pack()

radiobutton3 = ttk.Radiobutton(window, text='Male3', value=3)
radiobutton3.pack()

# Start the main event loop for the window
window.mainloop()
