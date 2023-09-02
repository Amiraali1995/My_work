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

# Create CheckButtons for female selection
checkbox1 = Checkbutton(window, text='Female1')
checkbox1.pack()

checkbox2 = Checkbutton(window, text='Female2')
checkbox2.pack()

checkbox3 = Checkbutton(window, text='Other ')
checkbox3.pack()

# Start the main event loop for the window
window.mainloop()
