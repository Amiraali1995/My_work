#import tkinter as tk
# Call the _test() function from the tkinter module
# This opens a test window with various widgets for interaction and testing
# tkinter._test()
from tkinter import *
# Import the tkinter library
import tkinter as tk
# Create an instance of the Tk class to create the main window
window = tk.Tk()
# Set the dimensions and position of the window
window.geometry('500x500+600+100')  # Width x Height + Left + Top
# Allow the window to be resized both horizontally and vertically
window.resizable(True, True)
# Set the title of the window
window.title("Amira's Window")

# Configure the background color of the window
window.config(background='grey')

# Set the window icon using an ICO file named 'a1.ico' in the same directory
window.iconbitmap('a1.ico')

# Start the main event loop to display the window and handle user interactions
window.mainloop()
