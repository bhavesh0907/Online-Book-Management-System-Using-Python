import mysql.connector

# Establish a connection to the MySQL server (Update credentials if needed)
db_connection = mysql.connector.connect(
    host="localhost",
    user="aryan",         # Replace with your MySQL username
    password="root@123"   # Replace with your MySQL password
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Create the 'library' database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS library")

# Use the 'library' database
cursor.execute("USE library")

# Create the 'books' table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) NOT NULL
)
"""
cursor.execute(create_table_query)

# Close the cursor and connection
cursor.close()
db_connection.close()

print("Database 'library' and table 'books' created successfully.")
