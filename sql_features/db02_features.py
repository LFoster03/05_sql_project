import sqlite3
import pathlib

# Function to execute SQL commands from a given file
def execute_sql_from_file(conn, file_path):
    """Execute SQL commands from a given file."""
    try:
        with open(file_path, 'r') as f:
            sql_script = f.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {file_path} successfully.")
    except sqlite3.Error as e:
        print(f"Error executing {file_path}: {e}")

# Function to create a database and establish a connection
def create_database(db_file):
    """Create a database file and establish a connection."""
    try:
        conn = sqlite3.connect(db_file)
        print(f"Successfully connected to database {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to {db_file}: {e}")
        return None

# Function to query data from the database
def query_data(conn):
    """Query data and demonstrate filtering, sorting, joining, and aggregation."""
    cursor = conn.cursor()

    # 1. Query to get all books with author details (Join operation)
    cursor.execute('''
        SELECT books.book_id, books.title, books.year_published, authors.first_name, authors.last_name
        FROM books
        JOIN authors ON books.author_id = authors.author_id
        ORDER BY books.year_published DESC;
    ''')
    print("Books with author details (sorted by year published):")
    for row in cursor.fetchall():
        print(row)

    # 2. Query to get the total number of books published by each author (Aggregation)
    cursor.execute('''
        SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS total_books
        FROM authors
        LEFT JOIN books ON authors.author_id = books.author_id
        GROUP BY authors.author_id;
    ''')
    print("\nTotal books published by each author:")
    for row in cursor.fetchall():
        print(row)

    # 3. Query to filter books published after 2015
    cursor.execute('''
        SELECT title, year_published
        FROM books
        WHERE year_published > 2015
        ORDER BY year_published;
    ''')
    print("\nBooks published after 2015:")
    for row in cursor.fetchall():
        print(row)

# Function to setup the database and execute operations
def setup_and_execute_operations(db_file):
    """Setup database and execute additional operations (update/delete)."""
    conn = create_database(db_file)
    if conn is None:
        return

    # Define the paths for the SQL files
    update_sql_path = pathlib.Path("sql_features", "update_records.sql")
    delete_sql_path = pathlib.Path("sql_features", "delete_records.sql")

    # Execute update operations
    execute_sql_from_file(conn, update_sql_path)

    # Execute delete operations
    execute_sql_from_file(conn, delete_sql_path)

    # Query the database to check updates and deletions
    query_data(conn)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Main function to run the operations
def main():
    db_file = "books_authors.db"  # Define the database file name
    setup_and_execute_operations(db_file)

if __name__ == "__main__":
    main()
