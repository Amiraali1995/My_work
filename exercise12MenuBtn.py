from tkinter import *
from tkinter import ttk

# Create the main window instance
window = Tk()

# Set the dimensions of the main window
window.geometry('600x400')

# Create a Menubutton widget for "LEARN"
menu1 = Menubutton(window, text='LEARN', relief='groove')
menu1.pack()

# Create a Menu for the Menubutton
submenu = Menu(menu1)
menu1['menu'] = submenu  # Associate the Menu with the Menubutton

# Add check buttons to the submenu
submenu.add_checkbutton(label='HTML')  # Check button for HTML
submenu.add_checkbutton(label='CSS')   # Check button for CSS
submenu.add_checkbutton(label='JavaScript')  # Check button for JavaScript

# Start the main event loop for the window
window.mainloop()
