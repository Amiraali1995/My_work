import tkinter as tk
from tkinter import messagebox
import webbrowser


class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x450+280+50')
        self.root.resizable(False, False)
        self.root.title('SUPERMARKET')
        self.root.iconbitmap('C:\\Users\\USER\\Desktop\\python_codes\\SqlSever_GUI_Python\\clogo.ico')
        self.create_gui()

    def create_gui(self):
        self.create_title()
        self.create_links_frame()
        self.create_supermarket_image()
        self.create_login_frame()

    def create_title(self):
        title = tk.Label(self.root, text='Super Market System', fg='gold', bg='black', font=('tajawal', 16, 'bold'))
        title.pack(fill=tk.X)

    def create_links_frame(self):
        frame1 = tk.Frame(self.root, width=230, height=425, bg='#0B2F3A')
        frame1.place(y=30)

        titles = ['Supermarket project', 'Developer Amire Ali', 'Contact us']
        buttons = ['Facebook Account', 'Linkedin Account', 'GitHup Account', 'About the Developer', 'Project Overview',
                   'Close the Program']
        commands = [self.open_facebook, self.open_linkedin, self.open_github, self.about_developer, self.about_system,
                    self.root.quit]

        for i, title in enumerate(titles):
            label = tk.Label(frame1, text=title, bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
            label.place(x=42, y=10 + 40 * i)

        for i, button_text in enumerate(buttons):
            button = tk.Button(frame1, text=button_text, width=23, fg='black', bg='#DBA901',
                               font=('tajawal', 11, 'bold'), command=commands[i])
            button.place(x=6, y=130 + 47 * i)

    def create_supermarket_image(self):
        photo = tk.PhotoImage(file='amarket.png')
        imo = tk.Label(self.root, image=photo, bg='white')
        imo.place(x=245, y=43, width=450, height=272)

    def create_login_frame(self):
        frame2 = tk.Frame(self.root, width=577, height=120, bg='#0B2F3A')
        frame2.place(x=229, y=330)

        photo1 = tk.PhotoImage(file='abc.png')
        imo1 = tk.Label(self.root, image=photo1)
        imo1.place(x=230, y=338, width=110, height=112)

        labels = ['Username', 'Password']
        entry_vars = [tk.StringVar(), tk.StringVar()]

        for i, label_text in enumerate(labels):
            label = tk.Label(frame2, text=label_text, fg='gold', bg='#0B2F3A', font=('tajawal', 12))
            label.place(x=120, y=25 + 45 * i)

            entry = tk.Entry(frame2, textvariable=entry_vars[i], font=('tajawal', 12), justify='center')
            entry.place(x=205, y=26 + 45 * i)

        login_button = tk.Button(frame2, text='Login', bg='#DBA901', font=('tajawal', 12), width=12, height=3,
                                 fg='black', command=self.login)
        login_button.place(x=420, y=20)

    def open_facebook(self):
        webbrowser.open_new('https://www.facebook.com')

    def open_linkedin(self):
        webbrowser.open_new('https://www.linkedin.com/in/amira-al-naamani-2b0818228/')

    def open_github(self):
        webbrowser.open_new('https://github.com/Amiraali1995')

    def about_developer(self):
        messagebox.showinfo('Developer', 'Amira Ali AL-Naamani')

    def about_system(self):
        messagebox.showinfo('About the System', 'SuperMarket Management System on Python Tkinter')

    def login(self):
        pass


# Implement your login logic here
# Retrieve the username and password from the entry widgets
# Compare them with your database or authentication system
# Display appropriate messages or actions based on the result

if __name__ == '__main__':
    window = tk.Tk()
    app = SupermarketApp(window)
    window.mainloop()
