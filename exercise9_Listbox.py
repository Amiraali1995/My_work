from tkinter import *
from tkinter import ttk

# Create the main window instance
window = Tk()

# Set the dimensions of the main window
window.geometry('600x400')

list1=Listbox(window)
list1.insert(0,'Python')
list1.insert(1,'Java')
list1.insert(2,'JavaScript')

list1.insert(3,'SQL')
list1.insert(4,'PHP')
list1.insert(5,'C++')
list1.pack()
# Start the main event loop for the window
window.mainloop()
