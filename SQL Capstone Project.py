# Import the sqlite3 library
import sqlite3

# Function to connect to the database
def connect_to_database():
    return sqlite3.connect("ebookstore.db")

# Function to create the books table in the database
def create_books_table(cursor):
    sql = """CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        qty INTEGER NOT NULL
    )"""
    cursor.execute(sql)

# Function to insert initial data into the books table
def insert_initial_data(cursor):
    # Sample data for books
    books_data = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
    sql = "INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)"
    cursor.executemany(sql, books_data)
    db.commit()

# Function to add a new book to the database
def add_book(cursor):
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    qty = int(input("Enter the quantity: "))

    sql = "INSERT INTO books (title, author, qty) VALUES (?, ?, ?)"
    values = (title, author, qty)
    cursor.execute(sql, values)
    db.commit()
    print("Book added successfully!\n")

# Function to update information about an existing book
def update_book(cursor):
    book_id = int(input("Enter the book ID you want to update: "))
    title = input("Enter the updated book title: ")
    author = input("Enter the updated author name: ")
    qty = int(input("Enter the updated quantity: "))

    sql = "UPDATE books SET title = ?, author = ?, qty = ? WHERE id = ?"
    values = (title, author, qty, book_id)
    cursor.execute(sql, values)
    db.commit()
    print("Book updated successfully!\n")

# Function to delete a book from the database
def delete_book(cursor):
    book_id = int(input("Enter the book ID you want to delete: "))
    sql = "DELETE FROM books WHERE id = ?"
    values = (book_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Book deleted successfully!\n")

# Function to search for books by title or author
def search_books(cursor):
    search_term = input("Enter the title or author to search: ")
    sql = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?"
    values = (f"%{search_term}%", f"%{search_term}%")
    cursor.execute(sql, values)
    result = cursor.fetchall()

    if not result:
        print("No matching books found.")
    else:
        print("Matching books:")
        for book in result:
            print(book)

# Main program
try:
    db = connect_to_database()
    cursor = db.cursor()

    create_books_table(cursor)
    insert_initial_data(cursor)

    while True:
        print("Select an option:")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search books")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book(cursor)
        elif choice == 2:
            update_book(cursor)
        elif choice == 3:
            delete_book(cursor)
        elif choice == 4:
            search_books(cursor)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

except sqlite3.Error as error:
    print("Error connecting to the database:", error)

finally:
    if db:
        db.close()
