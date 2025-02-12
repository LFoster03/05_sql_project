import sqlite3
import pathlib
import matplotlib.pyplot as plt

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

# Function to execute queries and display results
def execute_queries_and_display_results(conn):
    """Execute SQL queries and display or visualize the results."""
    cursor = conn.cursor()

    # 1. Aggregation Query: Count total number of books
    cursor.execute('SELECT COUNT(*) AS total_books FROM books')
    result = cursor.fetchone()
    print(f"Total number of books: {result[0]}")

    # 2. Aggregation Query: Average year of publication
    cursor.execute('SELECT AVG(year_published) AS avg_publication_year FROM books')
    result = cursor.fetchone()
    print(f"Average year of publication: {result[0]:.2f}")

    # 3. Aggregation Query: Total books per year
    cursor.execute('''
        SELECT year_published, COUNT(*) AS total_books_per_year
        FROM books
        GROUP BY year_published
        ORDER BY year_published DESC
    ''')
    books_per_year = cursor.fetchall()

    # Display the result
    print("\nTotal books published per year:")
    for row in books_per_year:
        print(row)

    # Visualization for Total Books Per Year
    years = [row[0] for row in books_per_year]
    total_books = [row[1] for row in books_per_year]
    plt.bar(years, total_books)
    plt.xlabel('Year')
    plt.ylabel('Total Books')
    plt.title('Total Books Published Per Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 4. Filtering Query: Get books published after 2015
    cursor.execute('SELECT * FROM books WHERE year_published > 2015')
    print("\nBooks published after 2015:")
    for row in cursor.fetchall():
        print(row)

    # 5. Sorting Query: Books sorted by year of publication (ascending)
    cursor.execute('SELECT * FROM books ORDER BY year_published ASC')
    print("\nBooks sorted by year of publication (ascending):")
    for row in cursor.fetchall():
        print(row)

    # 6. Grouping Query: Books published per author
    cursor.execute('''
        SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS total_books
        FROM authors
        JOIN books ON authors.author_id = books.author_id
        GROUP BY authors.author_id
        ORDER BY total_books DESC
    ''')
    books_per_author = cursor.fetchall()

    # Display the result
    print("\nTotal books published per author:")
    for row in books_per_author:
        print(row)

    # Visualization for Total Books Per Author
    authors = [f"{row[0]} {row[1]}" for row in books_per_author]
    total_books_per_author = [row[2] for row in books_per_author]
    plt.barh(authors, total_books_per_author)
    plt.xlabel('Total Books')
    plt.ylabel('Author')
    plt.title('Total Books Published Per Author')
    plt.tight_layout()
    plt.show()

    # 7. Join Query: List books with author names (INNER JOIN)
    cursor.execute('''
        SELECT books.title, books.year_published, authors.first_name, authors.last_name
        FROM books
        INNER JOIN authors ON books.author_id = authors.author_id
    ''')
    print("\nBooks with author details (INNER JOIN):")
    for row in cursor.fetchall():
        print(row)

    # 8. Join Query: Books with author names, including books with no authors (LEFT JOIN)
    cursor.execute('''
        SELECT books.title, books.year_published, authors.first_name, authors.last_name
        FROM books
        LEFT JOIN authors ON books.author_id = authors.author_id
    ''')
    print("\nBooks with author details (LEFT JOIN, including books without authors):")
    for row in cursor.fetchall():
        print(row)

# Function to setup the database and execute operations
def setup_and_execute_operations(db_file):
    """Setup database and execute queries."""
    conn = create_database(db_file)
    if conn is None:
        return

    # Define the paths for the SQL query files
    aggregation_sql_path = pathlib.Path("sql_queries", "query_aggregation.sql")
    filter_sql_path = pathlib.Path("sql_queries", "query_filter.sql")
    sorting_sql_path = pathlib.Path("sql_queries", "query_sorting.sql")
    group_by_sql_path = pathlib.Path("sql_queries", "query_group_by.sql")
    join_sql_path = pathlib.Path("sql_queries", "query_join.sql")

    # Execute the queries
    execute_sql_from_file(conn, aggregation_sql_path)
    execute_sql_from_file(conn, filter_sql_path)
    execute_sql_from_file(conn, sorting_sql_path)
    execute_sql_from_file(conn, group_by_sql_path)
    execute_sql_from_file(conn, join_sql_path)

    # Execute the queries and print/display results
    execute_queries_and_display_results(conn)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Main function to run the operations
def main():
    db_file = "books_authors.db"  # Define the database file name
    setup_and_execute_operations(db_file)

if __name__ == "__main__":
    main()
