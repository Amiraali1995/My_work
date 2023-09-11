from tkinter import *
from  tkinter import  ttk
import pyodbc
from tkinter import messagebox
class Student:

    def __init__(self,window):

        self.window=window
        self.window.geometry('1350x690+1+1')
        self.window.title('Schools Management System')
        self.window.configure(bg='silver')
        self.window.resizable(False,False)
        label_title=Label(window,
                    text='Student Registration System',
                    bg='#1AAECB',
                    font=('monospace',14,'bold'),
                    fg='white')
        label_title.pack(fill=X)

        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.qualifications_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.dell_var=StringVar()
        self.search_var = StringVar()



        manage_frame=Frame(self.window,bg='white')
        manage_frame.place(x=10,y=30,width=210,height=400)

        lbl_ID=Label(manage_frame,text='ID Number',bg='white')
        lbl_ID.pack()
        Id_Entry=Entry(manage_frame,textvariable=self.id_var,bd=2,justify='center',width=23)
        Id_Entry.pack()

        lbl_name=Label(manage_frame,bg='white',text='Student Name')
        lbl_name.pack()
        Name_Entry=Entry(manage_frame,textvariable=self.name_var,bd=2,justify='center',width=23)
        Name_Entry.pack()

        lbl_Phone = Label(manage_frame, bg='white', text='Student Phone Number')
        lbl_Phone.pack()
        Phone_Entry = Entry(manage_frame, textvariable=self.phone_var, bd=2, justify='center',width=23)
        Phone_Entry.pack()

        lbl_email = Label(manage_frame, bg='white', text='Student Email')
        lbl_email.pack()
        Email_Entry = Entry(manage_frame,textvariable=self.email_var, bd=2, justify='center',width=23)
        Email_Entry.pack()

        lbl_qualifications = Label(manage_frame, bg='white', text='Student qualifications')
        lbl_qualifications.pack()
        qualifications_Entry = Entry(manage_frame,textvariable=self.qualifications_var, bd=2, justify='center',width=23)
        qualifications_Entry.pack()

        lbl_gender=Label(manage_frame,text='Gender',bg='white')
        lbl_gender.pack()
        combobox_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var ,justify='center')
        combobox_gender['value']=('Male','Female')
        combobox_gender.pack()

        lbl_Address=Label(manage_frame,text='Student Address',bg='white')
        lbl_Address.pack()
        Address_Entry = Entry(manage_frame,textvariable=self.address_var, bd=2, justify='center',width=23)
        Address_Entry.pack()
        #delete by student name
        lbl_delete_byName = Label(manage_frame, text='Delete By Student Name ', bg='white',fg='red',)
        lbl_delete_byName.pack()
        Delete_Entry = Entry(manage_frame,textvariable=self.dell_var, bd=2, justify='center',width=23)
        Delete_Entry.pack()

        btn_frame=Frame(self.window,bg='white')
        btn_frame.place(x=10,y=435,width=210,height=255)
        title1=Label(btn_frame,text='Control Panel',font=('Deco',14,'bold'),fg='white',bg='#2980B9')
        title1.pack(fill=X)

        add_btn=Button(btn_frame,text='Add Student',bg='#85929e',fg='white',command=self.add_student)
        add_btn.place(x=33,y=45,width=150,height=30)

        del_btn = Button(btn_frame, text='Delete Student', bg='#85929e',fg='white',command=self.delete)
        del_btn.place(x=33,y=75,width=150,height=30)

        update_btn = Button(btn_frame, text='Update Student', bg='#85929e',fg='white',command=self.update)
        update_btn.place(x=33,y=105,width=150,height=30)

        clear_btn = Button(btn_frame, text='Clear Fields', bg='#85929e',fg='white',command=self.clear)
        clear_btn.place(x=33,y=135,width=150,height=30)

        about_btn = Button(btn_frame, text='About Us', bg='#85929e',fg='white',command=self.about)
        about_btn.place(x=33,y=165,width=150,height=30)

        exit_btn = Button(btn_frame, text='Exit', bg='red',fg='white',command=window.quit)
        exit_btn.place(x=33,y=195,width=150,height=30)


        search_frame=Frame(self.window,bg='white')
        search_frame.place(x=221,y=30,width=1135,height=50)
        lbl_search=Label(search_frame,text='Search for student ',bg='white')
        lbl_search.place(x=10,y=12)

        combobox_Search=ttk.Combobox(search_frame)
        combobox_Search['value']=('id','name','phone','email')
        combobox_Search.place(x=120,y=12)
        search_entry=Entry(search_frame,textvariable=self.search_var,justify='center',bd=2)
        search_entry.place(x=270,y=12)

        search_btn=Button(search_frame,text='Search',bg='#3498de',bd=2,fg='white',command=self.search)
        search_btn.place(x=400,y=12,width=100,height=20)


        details_frame=Frame(self.window,bg='#f2f4f4')
        details_frame.place(x=221,y=83,width=1134,height=605)
        scroll_x=Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(details_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(details_frame,
                                       columns=('id','name','phone','email','qualifications','gender','address'),
                                        xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table['show']='headings'
        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Student Name')
        self.student_table.heading('phone', text='Student Phone Number')
        self.student_table.heading('email', text='Student Email')
        self.student_table.heading('qualifications', text='Student qualifications')
        self.student_table.heading('gender', text='Student Gender')
        self.student_table.heading('address',text='Student Address')

        self.student_table.column('id', width=12)
        self.student_table.column('name', width=100)
        self.student_table.column('phone', width=65)
        self.student_table.column('email', width=70)
        self.student_table.column('qualifications', width=70)
        self.student_table.column('gender', width=30)
        self.student_table.column('address', width=130)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)


        self.fatch_all()

    def add_student(self):
        # Establish the connection
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()
        cursor.execute(
            "insert into student (id, name, phone, email, qualifications, gender, address) values (?, ?, ?, ?, ?, ?, ?)",
            (
                self.id_var.get(),
                self.name_var.get(),
                self.phone_var.get(),
                self.email_var.get(),
                self.qualifications_var.get(),
                self.gender_var.get(),
                self.address_var.get()))
        con.commit()
        self.fatch_all()
        con.close()
    def fatch_all(self):
        con=pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()
        cursor.execute('select * from student')
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,value=[str(val) for val in row])
                con.commit()
        con.close()


    def delete(self):
        con=pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;"
        )
        cursor = con.cursor()
        cursor.execute('delete from student where name=?',self.dell_var.get())
        con.commit()
        self.fatch_all()
        con.close()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.qualifications_var.set('')
        self.gender_var.set('')
        self.address_var.set('')
        self.dell_var.set('')
    def get_cursor(self,event):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.phone_var.set(row[2])
        self.email_var.set(row[3])
        self.qualifications_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    def update(self):
        selected_item = self.student_table.selection()
        if selected_item:
            con = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-VHP43PL\MSSQLS;"
                "Database=stud;"
                "Trusted_Connection=yes;")
            cursor = con.cursor()
            cursor.execute(
                "update student set name=?,phone=?,email=?,qualifications=?,gender=?,address=? where id=?",
                (
                    self.name_var.get(),
                    self.phone_var.get(),
                    self.email_var.get(),
                    self.qualifications_var.get(),
                    self.gender_var.get(),
                    self.address_var.get(),
                    self.id_var.get()
                ))
            con.commit()
            self.fatch_all()
            con.close()
        else:
            messagebox.showinfo("No Row Selected", "Please select a student to update.")

    def search(self):
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student WHERE name LIKE ?", ('%' + self.search_var.get() + '%',))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=[str(val) for val in row])
                con.commit()
        con.close()
    def about(self):
        messagebox.showinfo("developer amira ali","welcome to out first project")



window=Tk()
ob=Student(window)
window.mainloop()