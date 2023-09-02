from tkinter import *

# Create the main window
window = Tk()
window.geometry('500x400')

# Create a horizontal scale (scale1)
scale1 = Scale(window, from_=1, to=100, orient=HORIZONTAL)
scale1.place(x=300, y=10)

# Create a vertical scale (scale2)
scale2 = Scale(window, from_=1, to=100, orient=VERTICAL)
scale2.place(x=10, y=10)

# Create additional vertical scales (scale3, scale4, scale5) for demonstration
scale3 = Scale(window, from_=1, to=100, orient=VERTICAL)
scale3.place(x=50, y=10)

scale4 = Scale(window, from_=1, to=100, orient=VERTICAL)
scale4.place(x=110, y=10)

scale5 = Scale(window, from_=1, to=100, orient=VERTICAL)
scale5.place(x=170, y=10)

# Start the main event loop
window.mainloop()
