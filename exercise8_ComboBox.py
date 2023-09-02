from tkinter import *
from tkinter import ttk

# Create the main window instance
window = Tk()

# Set the dimensions of the main window
window.geometry('600x400')

# Create a combo box for gender selection
combo1 = ttk.Combobox(window, state='readonly', width=30,
                      values=('Female', 'Male', 'Other'))
combo1.place(x=1, y=1)  # Place the combo box at coordinates (1, 1)

# Create a combo box for country selection
combo2 = ttk.Combobox(window, state='readonly', width=30,
                      values=('Oman', 'Qatar', 'Saudi', 'UAE'))
combo2.place(x=1, y=40)  # Place the combo box at coordinates (1, 40)

# Start the main event loop for the window
window.mainloop()
