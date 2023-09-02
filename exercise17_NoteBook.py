from tkinter import *
from tkinter import ttk

# Create the main window
window = Tk()
window.geometry('500x400')

# Create a notebook (tabbed interface)
notebook1 = ttk.Notebook(window)
notebook1.pack()

# Create the first tab (HOME)
frame1 = Frame(notebook1, width='500', height='100', bg='Silver')
notebook1.add(frame1, text='HOME')

# Add content to the HOME tab
label1 = Label(frame1, text='LEARN PYTHON', bg='yellow')
label1.pack()

# Create the second tab (TOOLS)
frame2 = Frame(notebook1, width='500', height='100', bg='Silver')
notebook1.add(frame2, text='TOOLS')

# Add content to the TOOLS tab
label2 = Label(frame2, text='LEARN PYTHON', bg='red')
label2.pack()

# Select the second tab (TOOLS) by default
notebook1.select(frame2)

# Start the main event loop
window.mainloop()
