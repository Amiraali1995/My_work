from tkinter import *
from tkinter import ttk
import pyodbc
from tkinter import messagebox

class Student:

    def __init__(self, window):
        # Initialize the main window
        self.window = window
        self.window.geometry('1350x690+1+1')  # Set window size and position
        self.window.title('Schools Management System')  # Set window title

        # Create a title label
        label_title = Label(window,
                            text='Student Registration System',
                            bg='#2980B9',  # Background color
                            font=('Arial', 20, 'bold'),  # Font settings
                            fg='white')  # Text color
        label_title.pack(fill=X, pady=10)  # Pack the label and add padding

        # Define StringVars for data entry fields
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.qualifications_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.dell_var = StringVar()
        self.search_var = StringVar()

        # Create a frame for data entry and labels
        manage_frame = Frame(self.window, bg='#ECF0F1', bd=2, relief=RIDGE)
        manage_frame.place(x=10, y=60, width=340, height=460)

        # Labels and Entry widgets for ID, Name, Phone, Email, Qualifications, Gender, and Address
        lbl_ID = Label(manage_frame, text='ID Number', bg='#ECF0F1', font=('Arial', 12))
        lbl_ID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        Id_Entry = Entry(manage_frame, textvariable=self.id_var, bd=2, font=('Arial', 12))
        Id_Entry.grid(row=0, column=1, padx=10, pady=10)

        lbl_name = Label(manage_frame, text='Student Name', bg='#ECF0F1', font=('Arial', 12))
        lbl_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Name_Entry = Entry(manage_frame, textvariable=self.name_var, bd=2, font=('Arial', 12))
        Name_Entry.grid(row=1, column=1, padx=10, pady=10)

        lbl_Phone = Label(manage_frame, text='Phone Number', bg='#ECF0F1', font=('Arial', 12))
        lbl_Phone.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Phone_Entry = Entry(manage_frame, textvariable=self.phone_var, bd=2, font=('Arial', 12))
        Phone_Entry.grid(row=2, column=1, padx=10, pady=10)

        lbl_email = Label(manage_frame, text='Email', bg='#ECF0F1', font=('Arial', 12))
        lbl_email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Email_Entry = Entry(manage_frame, textvariable=self.email_var, bd=2, font=('Arial', 12))
        Email_Entry.grid(row=3, column=1, padx=10, pady=10)

        lbl_qualifications = Label(manage_frame, text='Qualifications', bg='#ECF0F1', font=('Arial', 12))
        lbl_qualifications.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        qualifications_Entry = Entry(manage_frame, textvariable=self.qualifications_var, bd=2, font=('Arial', 12))
        qualifications_Entry.grid(row=4, column=1, padx=10, pady=10)

        lbl_gender = Label(manage_frame, text='Gender', bg='#ECF0F1', font=('Arial', 12))
        lbl_gender.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        combobox_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var, values=('Male', 'Female'), font=('Arial', 12))
        combobox_gender.grid(row=5, column=1, padx=10, pady=10)

        lbl_Address = Label(manage_frame, text='Address', bg='#ECF0F1', font=('Arial', 12))
        lbl_Address.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        Address_Entry = Entry(manage_frame, textvariable=self.address_var, bd=2, font=('Arial', 12))
        Address_Entry.grid(row=6, column=1, padx=10, pady=10)

        # Entry for deleting a student by name
        lbl_delete_byName = Label(manage_frame, text='Delete By Name', bg='#ECF0F1', fg='red', font=('Arial', 12))
        lbl_delete_byName.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        Delete_Entry = Entry(manage_frame, textvariable=self.dell_var, bd=2, font=('Arial', 12))
        Delete_Entry.grid(row=7, column=1, padx=10, pady=10)

        # Create a frame for control buttons
        btn_frame = Frame(self.window, bg='#ECF0F1', bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=540, width=340, height=140)

        # Buttons for Add, Delete, Update, Clear, About Us, and Exit
        add_btn = Button(btn_frame, text='Add Student', bg='#2980B9', fg='white', font=('Arial', 12), command=self.add_student)
        add_btn.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        del_btn = Button(btn_frame, text='Delete Student', bg='#E74C3C', fg='white', font=('Arial', 12), command=self.delete)
        del_btn.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        update_btn = Button(btn_frame, text='Update Student', bg='#27AE60', fg='white', font=('Arial', 12), command=self.update)
        update_btn.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        clear_btn = Button(btn_frame, text='Clear Fields', bg='#ECF0F1', font=('Arial', 12), command=self.clear)
        clear_btn.grid(row=1, column=1, padx=20, pady=10, sticky='w')

        about_btn = Button(btn_frame, text='About Us', bg='#3498db', fg='white', font=('Arial', 12), command=self.about)
        about_btn.grid(row=2        , column=0, padx=20, pady=10, sticky='w')

        exit_btn = Button(btn_frame, text='Exit', bg='#F39C12', fg='white', font=('Arial', 12), command=window.quit)
        exit_btn.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        # Create a frame for searching
        search_frame = Frame(self.window, bg='#ECF0F1', bd=2, relief=RIDGE)
        search_frame.place(x=360, y=60, width=1005, height=60)

        # Label and Entry for searching students
        lbl_search = Label(search_frame, text='Search for student', bg='#ECF0F1', font=('Arial', 12))
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        combobox_Search = ttk.Combobox(search_frame, textvariable=self.search_var, values=('id', 'name', 'phone', 'email'), font=('Arial', 12))
        combobox_Search.grid(row=0, column=1, padx=10, pady=10)

        search_entry = Entry(search_frame, bd=2, font=('Arial', 12))
        search_entry.grid(row=0, column=2, padx=10, pady=10)

        search_btn = Button(search_frame, text='Search', bg='#3498db', fg='white', font=('Arial', 12), command=self.search)
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create a frame for displaying student details
        details_frame = Frame(self.window, bg='#ECF0F1', bd=2, relief=RIDGE)
        details_frame.place(x=360, y=130, width=1005, height=550)

        # Scrollbars for the Treeview widget
        scroll_x = Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(details_frame, orient=VERTICAL)

        # Create a Treeview widget for displaying student details
        self.student_table = ttk.Treeview(details_frame,
                                          columns=('id', 'name', 'phone', 'email', 'qualifications', 'gender', 'address'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        self.student_table.place(x=18, y=1, width=970, height=535)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Set Treeview column headings
        self.student_table['show'] = 'headings'
        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Student Name')
        self.student_table.heading('phone', text='Phone Number')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('qualifications', text='Qualifications')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('address', text='Address')

        # Set column widths
        self.student_table.column('id', width=12)
        self.student_table.column('name', width=150)
        self.student_table.column('phone', width=100)
        self.student_table.column('email', width=150)
        self.student_table.column('qualifications', width=100)
        self.student_table.column('gender', width=50)
        self.student_table.column('address', width=200)

        # Bind a function to left-click event on the Treeview
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch and display all student records
        self.fetch_all()

    def add_student(self):
        # Establish a database connection
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()

        # Insert student data into the database
        cursor.execute(
            "insert into student (id, name, phone, email, qualifications, gender, address) values (?, ?, ?, ?, ?, ?, ?)",
            (
                self.id_var.get(),
                self.name_var.get(),
                self.phone_var.get(),
                self.email_var.get(),
                self.qualifications_var.get(),
                self.gender_var.get(),
                self.address_var.get()
            ))
        con.commit()
        con.close()

        # Fetch and display updated student records
        self.fetch_all()

    def fetch_all(self):
        # Establish a database connection
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()

        # Retrieve all student records from the database
        cursor.execute('select * from student')
        rows = cursor.fetchall()

        # Clear existing data in the Treeview widget
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

            # Insert retrieved data into the Treeview without quotes
            for row in rows:
                row_without_quotes = [str(val) for val in row]
                self.student_table.insert("", END, values=row_without_quotes)
                con.commit()

        con.close()

    def delete(self):
        # Establish a database connection
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()

        # Delete a student record based on the provided name
        cursor.execute('delete from student where name=?', self.dell_var.get())
        con.commit()
        con.close()

        # Fetch and display updated student records
        self.fetch_all()

    def clear(self):
        # Clear data in the input fields
        self.id_var.set('')
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.qualifications_var.set('')
        self.gender_var.set('')
        self.address_var.set('')

    def get_cursor(self, event):
        # Get the selected student's details and populate the input fields
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.phone_var.set(row[2])
        self.email_var.set(row[3])
        self.qualifications_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    def update(self):
        # Check if a row is selected in the Treeview
        selected_item = self.student_table.selection()

        if selected_item:
            # Establish a database connection
            con = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-VHP43PL\MSSQLS;"
                "Database                =stud;"
                "Trusted_Connection=yes;")
            cursor = con.cursor()

            # Update the selected student's record
            cursor.execute(
                "update student set name=?, phone=?, email=?, qualifications=?, gender=?, address=? where id=?",
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
            con.close()

            # Fetch and display updated student records
            self.fetch_all()
        else:
            messagebox.showinfo("No Row Selected", "Please select a student to update.")

    def search(self):
        # Establish a database connection
        con = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-VHP43PL\MSSQLS;"
            "Database=stud;"
            "Trusted_Connection=yes;")
        cursor = con.cursor()

        # Search for students based on the selected search criteria
        if self.search_var.get() == 'id':
            cursor.execute("SELECT * FROM student WHERE id LIKE ?", ('%' + self.search_var.get() + '%',))
        elif self.search_var.get() == 'name':
            cursor.execute("SELECT * FROM student WHERE name LIKE ?", ('%' + self.search_var.get() + '%',))
        elif self.search_var.get() == 'phone':
            cursor.execute("SELECT * FROM student WHERE phone LIKE ?", ('%' + self.search_var.get() + '%',))
        elif self.search_var.get() == 'email':
            cursor.execute("SELECT * FROM student WHERE email LIKE ?", ('%' + self.search_var.get() + '%',))

        rows = cursor.fetchall()

        # Clear existing data in the Treeview widget
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

            # Insert retrieved data into the Treeview
            for row in rows:
                self.student_table.insert("", END, values=row)
                con.commit()

        con.close()

    def about(self):
        messagebox.showinfo("Developer: Amira Ali", "Welcome to our first project")

# Create the main window
window = Tk()
window.title('Student Registration System')
window.geometry('1366x768')  # Set window size
window.configure(bg='#ECF0F1')  # Set background color

# Create an instance of the Student class
app = Student(window)

# Start the Tkinter event loop
window.mainloop()


