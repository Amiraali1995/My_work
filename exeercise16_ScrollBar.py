from tkinter import *

# Create the main window
window = Tk()
window.geometry('500x400')

# Create a vertical scrollbar (scrollBar1)
scrollBar1 = Scrollbar(window, orient=VERTICAL)
scrollBar1.pack(side=RIGHT, fill=Y)  # Position the scrollbar on the right side and fill in the vertical direction.

# Create a horizontal scrollbar (scrollBar2)
scrollBar2 = Scrollbar(window, orient=HORIZONTAL)
scrollBar2.pack(side=BOTTOM, fill=X)  # Position the scrollbar at the bottom and fill in the horizontal direction.

# Start the main event loop
window.mainloop()
