from tkinter import *

# Create two window instances
window1 = Tk()
window2 = Tk()

# Set titles for the windows
window1.title('Window 1')

# Raise the visibility of window1 above other windows
window1.lift()

# Iconify (minimize) window2 to hide it from the user
window2.iconify()

# Lower window2 below other windows (hidden, but still in taskbar)
window2.lower()

# Change window2 to iconic state (minimized) - hidden from user
window2.state('iconic')

# Change window2 to normal state (restored from minimized)
window2.state('normal')

# Change window2 to withdrawn state (hidden from user and taskbar)
window2.state('withdrawn')

# Start the main event loop for the windows
window1.mainloop()
window2.mainloop()  # This won't run because window2 is withdrawn
