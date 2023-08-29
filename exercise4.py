"""
In the provided code example, two frames (frame1 and frame2) are created within the main window.
Each frame serves as a container that can hold other widgets or elements.
The frames themselves can have their own properties, such as dimensions and background colors,
which can help visually distinguish different sections of the user interface.
"""
from tkinter import *

# Create the main window instance
window = Tk()

# Set the dimensions and title of the main window
window.geometry('800x500')
window.title('Frames')

# Create the first frame with specified dimensions and background color
frame1 = Frame(width='390', height='499', bg='green')
# Place the first frame at coordinates (1, 1) within the main window
frame1.place(x=1, y=1)

# Create the second frame with specified dimensions and background color
frame2 = Frame(width='390', height='499', bg='blue')
# Place the second frame at coordinates (399, 1) within the main window
frame2.place(x=399, y=1)

# Start the main event loop for the window
window.mainloop()
