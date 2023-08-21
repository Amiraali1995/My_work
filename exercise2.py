# Import the entire tkinter module
from tkinter import *

# Create the first window instance
window1 = Tk()
# Create the second window instance
window2 = Tk()
# Set titles for the windows
window1.title('Window 1')
window2.title('Window 2')
# Set the dimensions and positions of the windows
window1.geometry('300x300+10+10')  # Width x Height + Left + Top
window2.geometry('300x300+320+10')  # Width x Height + Left + Top
# Configure the background color for the windows
window1.config(bg='red')
window2.config(bg='blue')

# Start the main event loop for the first window
window1.mainloop()
