import tkinter as tk
from tkinter import messagebox


# Function to display a message based on selected options
def show_message():
    message = "Selected Options:\n"

    # Checkboxes
    if var_python.get():
        message += "- Python\n"
    if var_java.get():
        message += "- Java\n"
    if var_cpp.get():
        message += "- C++\n"

    # Radiobuttons
    if selected_language.get() == 1:
        message += "- English\n"
    elif selected_language.get() == 2:
        message += "- Arabic\n"
    elif selected_language.get() == 3:
        message += "- French\n"

    # Listbox
    selected_books = listbox.curselection()
    for index in selected_books:
        message += f"- {book_list[index]}\n"

    # Entry Box
    name = entry_name.get()
    if name:
        message += f"- Name: {name}\n"

    # Display the message in a messagebox
    if message == "Selected Options:\n":
        message = "No options selected."
    messagebox.showinfo("Selections", message)


# Create the main window
window = tk.Tk()
window.title("Selections")

# Checkboxes
var_python = tk.BooleanVar()
var_java = tk.BooleanVar()
var_cpp = tk.BooleanVar()

checkbox_python = tk.Checkbutton(window, text="Python", variable=var_python)
checkbox_java = tk.Checkbutton(window, text="Java", variable=var_java)
checkbox_cpp = tk.Checkbutton(window, text="C++", variable=var_cpp)

# Radiobuttons
selected_language = tk.IntVar()

radio_english = tk.Radiobutton(window, text="English", variable=selected_language, value=1)
radio_spanish = tk.Radiobutton(window, text="Spanish", variable=selected_language, value=2)
radio_french = tk.Radiobutton(window, text="French", variable=selected_language, value=3)

# Listbox
book_list = ["Python Basics", "Java Programming", "C++ Crash Course", "JavaScript Fundamentals"]
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=len(book_list))
for book in book_list:
    listbox.insert(tk.END, book)

# Entry Box
entry_name = tk.Entry(window, width=30)

# Button to display selections
show_button = tk.Button(window, text="Show Selections", command=show_message)

# Layout using grid
checkbox_python.grid(row=0, column=0, sticky="w")
checkbox_java.grid(row=1, column=0, sticky="w")
checkbox_cpp.grid(row=2, column=0, sticky="w")

radio_english.grid(row=0, column=1, sticky="w")
radio_spanish.grid(row=1, column=1, sticky="w")
radio_french.grid(row=2, column=1, sticky="w")

listbox.grid(row=3, column=0, columnspan=2)

entry_name.grid(row=4, column=0, columnspan=2)

show_button.grid(row=5, column=0, columnspan=2)

# Start the main event loop
window.mainloop()
