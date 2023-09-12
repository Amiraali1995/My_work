from tkinter import *
from tkinter import ttk

# Create the main window
window = Tk()
window.geometry('500x500')
window.title('LOGIN SYSTEM')
window.config(bg='#D5DBDB')
window.resizable(False, False)
window.iconbitmap('C:\\Users\\USER\\Desktop\\python_codes\\SqlSever_GUI_Python\\ab.ico')

# Title Label
titleLabel = Label(window, text='LOGIN SYSTEM', font=('Courier', 15, 'bold'), bg='black', fg='white')
titleLabel.pack(fill=X)

# Frame for login elements
frame1 = Frame(window, width='300', height='350', bg='#F5F5F5')
frame1.pack(pady=30)

# Load and display an image
photo = PhotoImage(file='C:\\Users\\USER\\Desktop\\python_codes\\SqlSever_GUI_Python\\aa.png')
resizeImg = photo.subsample(2, 3)
panel = Label(window, image=resizeImg)
panel.place(x=200, y=60)

# Label and Entry for Username
labelUserName = Label(frame1, text='USERNAME: ', font=('Courier', 15), bg='#F5F5F5')
labelUserName.place(x=10, y=140)
entryUsername = Entry(frame1)
entryUsername.place(x=134, y=145)

# Label and Entry for Password
labelPassword = Label(frame1, text='PASSWORD: ', font=('Courier', 15), bg='#F5F5F5')
labelPassword.place(x=10, y=180)
entryPassword = Entry(frame1)
entryPassword.place(x=134, y=185)

# Login Button
btn_Login = Button(frame1, text='LOGIN', font=('Courier', 15), bg='grey', width='11',)
btn_Login.place(x=15, y=260)

# Signup Button
btn_SignUp = Button(frame1, text='SIGNUP', font=('Courier', 15), bg='grey', width='11')
btn_SignUp.place(x=155, y=260)

# Checkbox for Forget Password
cb_ForgetPWD = Checkbutton(frame1, text='Forget Password ', font=('Courier', 13, 'underline'), bg='#F5F5F5', fg='red')
cb_ForgetPWD.place(x=40, y=220)

# Developer Label
lb1 = Label(frame1, text='Developed by AMIRA 2023 ', font=('Courier', 8, 'bold'), bg='#F5F5F5', fg='red')
lb1.place(x=60, y=320)

# Start the main event loop
window.mainloop()
