from tkinter import *

# Create the main window
window =Tk()
window.title("To-Do List")

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

# Function to remove a selected task
def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Entry widget to enter tasks
entry = Entry(window, width=30)
entry.pack(pady=10)

# Button to add tasks
add_button = Button(window, text="Add Task", command=add_task)
add_button.pack()

# Button to remove selected task
remove_button = Button(window, text="Remove Task", command=remove_task)
remove_button.pack()

# Listbox to display tasks
listbox = Listbox(window, selectmode=SINGLE,width=30)
listbox.pack()

# Start the main event loop
window.mainloop()
