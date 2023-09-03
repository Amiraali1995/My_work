from tkinter import *
from tkinter import ttk

# Create the main window
window = Tk()
window.geometry('500x500')

# Load an image using PhotoImage
photo = PhotoImage(file=r'C:\\Users\\USER\\Pictures\\cc.png')

# Resize the image using subsample
resizeImg = photo.subsample(2, 3)

# Create a button with text, image, and image placement
button = Button(window, text='LEARN PYTHON', image=resizeImg, compound=TOP)
button.pack()

# Start the main event loop
window.mainloop()
