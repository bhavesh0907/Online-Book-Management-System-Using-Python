# Online Book Management System

## Overview
The **Online Book Management System** is a Python-based GUI application that enables users to manage a book database efficiently. It allows users to add books with details like title, author, and ISBN into a MySQL database through a simple Tkinter interface. 📚

## Features
- 📖 **Add Books** – Input book details such as title, author, and ISBN.
- 🗃 **Database Integration** – Stores and retrieves book data from a MySQL database.
- 🔍 **Search Functionality** – Look up books by title or author.
- 🖥 **Tkinter-Based GUI** – Provides an easy-to-use graphical interface.
- ⚡ **Efficient Management** – Enables smooth handling of large book collections.

## Repository Structure
```
Book-Management-System/
│── src/                  # Source code files
│── db/                   # MySQL database scripts
│── docs/                 # Documentation
│── main.py               # Main application file
│── config.py             # Database configuration file
│── README.md             # Project documentation
```

## Technologies Used
- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Database**: MySQL
- **Development Tools**: MySQL Connector, Pandas

## Installation & Usage
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- MySQL Database
- Required Python Libraries: `tkinter`, `mysql-connector-python`, `pandas`

### Setup & Run
```bash
# Clone the repository
git clone https://github.com/your-username/Book-Management-System.git

# Navigate to the project directory
cd Book-Management-System

# Configure database settings in config.py

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage
1. **Launch the Book Management System**
   ```bash
   python main.py
   ```
2. **Add book details** – Enter the title, author, and ISBN.
3. **Search for books** – Find books based on title or author.
4. **Manage the book database** – Update or delete book records as needed.
5. **Exit the application** when done.

## Contributors
- **Bhavesh Mishra** *(Lead Developer)*

## Contributing
Contributions are welcome! If you find any issues or want to improve the project, feel free to fork the repository and submit a pull request.

---
Developed with ❤️ to simplify book management using Python.
