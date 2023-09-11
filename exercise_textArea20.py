# Import the tkinter library
from tkinter import *
import tkinter as tk

# Create the main window
window = Tk()

# Set the dimensions of the main window
window.geometry('500x500')

# Create a Text widget within the main window
textArea = tk.Text(window)

# Pack the Text widget into the main window
textArea.pack()

# Define some text content
learn = """
Let's learn HTML
Let's learn CSS
Let's learn PHP
Python is very easy
"""

# Insert the text content into the Text widget
textArea.insert(tk.END, learn)

# Start the GUI application's main event loop
window.mainloop()
