import tkinter as tk
from tkinter import ttk
import pyodbc

# Function to refresh the treeview with updated records
def refresh_treeview():
    tree.delete(*tree.get_children())  # Clear existing data from the treeview
    cursor.execute("SELECT * FROM Products")  # Retrieve all records from the Products table
    records = cursor.fetchall()  # Fetch all records
    for record in records:
        formatted_record = [str(item) for item in record]  # Convert record values to strings
        tree.insert("", "end", values=formatted_record)  # Insert each record into the treeview

# Function to insert a new record
def insert_record():
    name = name_entry.get()  # Get value from the Name entry box
    price = price_entry.get()  # Get value from the Price entry box
    cursor.execute("INSERT INTO Products (Name, Price) VALUES (?, ?)", (name, price))  # Insert new record
    conn.commit()  # Commit the transaction to the database
    refresh_treeview()  # Refresh the treeview to display the updated records

# Function to update a record
def update_record():
    selected_item = tree.selection()[0]  # Get the selected item from the treeview
    values = tree.item(selected_item, "values")  # Get the values of the selected item
    new_name = name_entry.get()  # Get new value from the Name entry box
    new_price = price_entry.get()  # Get new value from the Price entry box
    cursor.execute("UPDATE Products SET Name = ?, Price = ? WHERE ID = ?", (new_name, new_price, values[0]))  # Update the selected record
    conn.commit()  # Commit the transaction to the database
    refresh_treeview()  # Refresh the treeview to display the updated records

# Function to delete a record
def delete_record():
    selected_item = tree.selection()[0]  # Get the selected item from the treeview
    values = tree.item(selected_item, "values")  # Get the values of the selected item
    cursor.execute("DELETE FROM Products WHERE ID = ?", (values[0],))  # Delete the selected record
    conn.commit()  # Commit the transaction to the database
    refresh_treeview()  # Refresh the treeview to display the updated records

# Create the main window
root = tk.Tk()
root.title("Product Records")

# Create a treeview to display data
tree = ttk.Treeview(root, columns=("ID", "Name", "Price"))
tree.heading("#1", text="ID")
tree.heading("#2", text="Name")
tree.heading("#3", text="Price")
tree.pack()

# Connect to the database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-VHP43PL\MSSQLS;'
                      'Database=ProductDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()  # Create a cursor for executing SQL commands

# Create buttons, labels, and entry boxes
refresh_button = tk.Button(root, text="Refresh", command=refresh_treeview)
refresh_button.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

price_label = tk.Label(root, text="Price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

insert_button = tk.Button(root, text="Insert", command=insert_record)
insert_button.pack()

update_button = tk.Button(root, text="Update", command=update_record)
update_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_record)
delete_button.pack()

refresh_treeview()  # Initial refresh to display existing records

root.mainloop()  # Start the GUI event loop
