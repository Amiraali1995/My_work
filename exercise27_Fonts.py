# Import the tkinter library
from tkinter import *

# Create a main window
window = Tk()

# Set the dimensions of the main window
window.geometry('500x500')

# Create a label with underlined text using 'Time New Roman' font
label1 = Label(window, text='LEARN PYTHON 2020', font=('Time New Roman', 12, 'underline'))
label1.pack()

# Create a label with bold text using 'Helvetica' font
label2 = Label(window, text='LEARN PYTHON 2021', font=('Helvetica', 12, 'bold'))
label2.pack()

# Create a label with italicized text using 'Impact' font
label3 = Label(window, text='LEARN PYTHON Tkinter 2022', font=('Impact', 12, 'italic'))
label3.pack()

# Start the main event loop to display the window
window.mainloop()
