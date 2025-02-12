import sqlite3
import pathlib
import os
import pandas as pd


# Function to execute SQL commands from a file
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

# Function to setup the database schema by running SQL scripts
def setup_database(db_file):
    """Setup database schema by running SQL scripts."""
    conn = create_database(db_file)
    if conn is None:
        return

    # Define the paths for the SQL files
    drop_sql_path = pathlib.Path("sql_create", "01_drop_tables.sql")
    create_sql_path = pathlib.Path("sql_create", "02_create_tables.sql")
    insert_sql_path = pathlib.Path("sql_create", "03_insert_records.sql")

    # Drop the existing tables
    execute_sql_from_file(conn, drop_sql_path)

    # Create the tables
    execute_sql_from_file(conn, create_sql_path)

    # Insert records into the tables
    execute_sql_from_file(conn, insert_sql_path)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to create the necessary SQL files for setup
def create_sql_files():
    """Create SQL files for setting up the database."""
    # 01_drop_tables.sql
    drop_sql = """
    DROP TABLE IF EXISTS books;
    DROP TABLE IF EXISTS authors;
    """
    with open("sql_create/01_drop_tables.sql", "w") as f:
        f.write(drop_sql)

    # 02_create_tables.sql
    create_sql = """
    CREATE TABLE authors (
        author_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );

    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        year_published INTEGER,
        author_id TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
    """
    with open("sql_create/02_create_tables.sql", "w") as f:
        f.write(create_sql)

    # 03_insert_records.sql
    insert_sql = """
    INSERT INTO authors (author_id, first_name, last_name)
    VALUES
        ('F301', 'Delia', 'Bowman'),
        ('F302', 'Erin', 'Morgenstern'),
        ('F303', 'Donna', 'Tartt'),
        ('F304', 'Alex', 'Michaelides'),
        ('F305', 'Liane', 'Moriarty'),
        ('F306', 'Sally', 'Rooney'),
        ('F307', 'Matt', 'Haig'),
        ('F308', 'Celeste', 'Ng'),
        ('F309', 'Taylor', 'Jenkins Reid'),
        ('F310', 'Madeline', 'Miller');

    INSERT INTO books (book_id, title, year_published, author_id)
    VALUES
        (1, 'Where the Crawdads Sing', 2018, 'F301'),
        (2, 'The Night Circus', 2011, 'F302'),
        (3, 'The Goldfinch', 2013, 'F303'),
        (4, 'The Silent Patient', 2019, 'F304'),
        (5, 'Big Little Lies', 2014, 'F305'),
        (6, 'Normal People', 2018, 'F306'),
        (7, 'The Midnight Library', 2020, 'F307'),
        (8, 'Little Fires Everywhere', 2017, 'F308'),
        (9, 'The Seven Husbands of Evelyn Hugo', 2017, 'F309'),
        (10, 'Circe', 2018, 'F310');
    """
    with open("sql_create/03_insert_records.sql", "w") as f:
        f.write(insert_sql)

# Main function to run the setup
def main():
    db_file = "books_authors.db"  # Define the database file name

    # Create the necessary SQL files for setup
    create_sql_files()

    # Setup the database
    setup_database(db_file)

if __name__ == "__main__":
    main()

