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

# Create a button within the first frame
button1 = Button(frame1, text='Button1', fg='black', bg='blue', cursor='heart', width=30)
# Place the button at coordinates (10, 10) within the first frame
button1.place(x=10, y=10)

# Create a button within the second frame
button2 = Button(frame2, text='Button2', fg='black', bg='green', cursor='heart', width=30)
# Place the button at coordinates (10, 10) within the second frame
button2.place(x=10, y=10)

# Create a label within the first frame
label1 = Label(frame1, text='This is frame 1', fg='black', bg='white', font=10)
# Place the label at coordinates (10, 40) within the first frame
label1.place(x=10, y=40)

# Create a label within the second frame
label2 = Label(frame2, text='This is frame 2', fg='black', bg='white', font=10)
# Place the label at coordinates (10, 40) within the second frame
label2.place(x=10, y=40)

entry1=Entry(frame1)
entry1.place(x=10,y=100)

entry2=Entry(frame1,justify='center')
entry2.place(x=10,y=140)

entry3=Entry(frame1,justify='center',fg='red',bg='black')
entry3.place(x=10,y=180)

entry4=Entry(frame1,justify='center',fg='red',bg='yellow',font=10)
entry4.place(x=10,y=220)

entry5=Entry(frame2)
entry5.place(x=10,y=100)


# Start the main event loop for the window
window.mainloop()
