from tkinter import *


class Super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700+30+10')
        self.root.title('Supermarket: Project Management')
        self.root.resizable(False, False)
        self.root.iconbitmap('icon_super.ico')

        title = Label(self.root, text='Project Management: Supermarket', bg='#0b2f3a', fg='white',
                      font=('tajawal', 15, 'bold'))
        title.pack(fill=X)

        # Adjusted the placement of the frame to the left
        F1 = Frame(root, bd=2, width=338, height=170, bg='#0b4c5f')
        F1.place(x=0, y=30)

        tit = Label(F1, text='Buyer Information:', font=('tajawal', 13, 'bold'), bg='#0b4c5f', fg='tomato')
        tit.place(x=5, y=0)

        buyer_name = Label(F1, text='Buyer Name', font=('tajawal', 10, 'bold'), bg='#0b4c5f', fg='white')
        buyer_name.place(x=5, y=40)

        buyer_phone = Label(F1, text='Buyer Phone', font=('tajawal', 10, 'bold'), bg='#0b4c5f', fg='white')
        buyer_phone.place(x=5, y=70)

        invoice_number = Label(F1, text='Invoice Number', font=('tajawal', 10, 'bold'), bg='#0b4c5f', fg='white')
        invoice_number.place(x=5, y=100)

        buyer_name_entry = Entry(F1, font=('tajawal', 10))
        buyer_name_entry.place(x=120, y=40)

        buyer_phone_entry = Entry(F1, font=('tajawal', 10))
        buyer_phone_entry.place(x=120, y=70)

        invoice_number_entry = Entry(F1, font=('tajawal', 10))
        invoice_number_entry.place(x=120, y=100)

        search_button = Button(F1, text='Search', bg='white', font=('tajawal', 10), fg='black')
        search_button.place(x=275, y=40)

        titdd = Label(F1, text='[ Invoices ]', font=('tajawal', 13, 'bold'), bg='#0b4c5f', fg='gold')
        titdd.place(x=120, y=130)

        F3 = Frame(root, bd=2, width=338, height=399, bg='white')
        F3.place(x=0, y=205)





root = Tk()
ob = Super(root)

root.mainloop()
