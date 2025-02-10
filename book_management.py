import tkinter as tk
import mysql.connector

# Create a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="aryan",         # Replace with your MySQL username
    password="root@123",  # Replace with your MySQL password
    database="library"
)

# Create a cursor
cursor = db.cursor()

# Function to add a book to the database
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()

    if title and author and isbn:  # Ensure no empty fields
        sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
        values = (title, author, isbn)
        cursor.execute(sql, values)
        db.commit()
        status_label.config(text="✅ Book added successfully!", fg="green")
    else:
        status_label.config(text="⚠️ Please fill all fields.", fg="red")

# Function to close database connection when the window is closed
def on_closing():
    cursor.close()
    db.close()
    window.destroy()

# Create the main application window
window = tk.Tk()
window.title("📚 Library Management System")

# Labels and Entry Fields
tk.Label(window, text="📖 Title:").pack()
title_entry = tk.Entry(window)
title_entry.pack()

tk.Label(window, text="✍️ Author:").pack()
author_entry = tk.Entry(window)
author_entry.pack()

tk.Label(window, text="🔢 ISBN:").pack()
isbn_entry = tk.Entry(window)
isbn_entry.pack()

# Add Book Button
add_button = tk.Button(window, text="➕ Add Book", command=add_book, bg="blue", fg="white")
add_button.pack()

# Status Label
status_label = tk.Label(window, text="", font=("Arial", 10))
status_label.pack()

# Handle window close event
window.protocol("WM_DELETE_WINDOW", on_closing)

# Run the GUI application
window.mainloop()
