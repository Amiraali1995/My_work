# Import the tkinter library
from tkinter import *
from tkinter import messagebox  # Import the messagebox module

# Create the main window
window = Tk()

# Set the dimensions of the main window
window.geometry('400x400')

# Define a function 'info' to display an information message in a messagebox
def info():
    # Use the 'showinfo' method from the 'messagebox' module to show an information dialog
    messagebox.showinfo('Information', 'Name: Amira\nAge: 27')

# Define a function 'info1' to display a warning message in a messagebox
def info1():
    # Use the 'showwarning' method from the 'messagebox' module to show a warning dialog
    messagebox.showwarning('Warning', 'Name: Amira\nAge: 27')

# Define a function 'info2' to display an error message in a messagebox
def info2():
    # Use the 'showerror' method from the 'messagebox' module to show an error dialog
    messagebox.showerror('Error', 'Name: Amira\nAge: 27')

# Define a function 'info3' to ask for user input with an OK/Cancel dialog
def info3():
    # Use the 'askokcancel' method from the 'messagebox' module to show an OK/Cancel dialog
    response = messagebox.askokcancel('OK or Cancel', 'Do you want to proceed?\nName: Amira\nAge: 27')
    if response:
        print('User clicked OK')
    else:
        print('User clicked Cancel')

def info4():
    # Use the 'showerror' method from the 'messagebox' module to show an error dialog
    messagebox.askyesno('ask', 'Name: Amira\nAge: 27')

def info5():
    # Use the 'showerror' method from the 'messagebox' module to show an error dialog
    messagebox.askquestion('ask', 'Name: Amira\nAge: 27')

# Create buttons in the main window to trigger the respective functions
btn1 = Button(window, text='Info', command=info)
btn1.pack()

btn2 = Button(window, text='Warning', command=info1)
btn2.pack()

btn3 = Button(window, text='Error', command=info2)
btn3.pack()

btn4 = Button(window, text='Ask Message', command=info3)
btn4.pack()

btn5 = Button(window, text='Ask Question', command=info4)
btn5.pack()

btn5 = Button(window, text='Ask Question', command=info4)
btn5.pack()


# Start the GUI application's main event loop
window.mainloop()
