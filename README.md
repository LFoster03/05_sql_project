# 05_sql_project

# SQL Project Module 5
This project is used to experiment with SQL.

## Add/Update Critical Files
Added and updated critical files. 

Add/Add .gitignore
The .gitignore file tells Git files to ignore when committing changes.
Review/copy the example .gitignore file, you might be able to use it without modification.
Add/Update requirements.txt
The requirements.txt file lists the packages used in the project.
Review/copy the example requirements.txt file, you might be able to use it without modification.
You may not need all the listed packages - and may want to add others. Modify the requirements.txt as needed.
Update README.md
Edit and customize your README.md to provide an overview of the project and instructions for running it.
Git add-commit-push
After adding .gitignore (or any other key file), run git add, commit, and push to commit your changes to GitHub.

## Setup Virtual Environment 
On Mac/Linux, Use zsh or bash (or PowerShell):
python3 -m venv .venv

### If VS Code asks: We noticed a new environment has been created. 
Do you want to select it for the workspace folder?
Click Yes. 

## Activate virtual environment
source .venv/bin/activate

## Schema Design and Database Initialization
Design a schema with at least two related tables, including foreign key constraints. Document the schema design in your README.md.

sql_create folder:

01_drop_tables.sql - drop tables to restart
02_create_tables.sql - create your database schema using sql
03_insert_records.sql - insert at least 10 additional records into each table.
db01_setup.py:

Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. Make it easy to re-run by dropping the tables first.

## Cleaning and Feature Engineering
Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements. You might create an additional table, insert new records, and perform data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.

sql_features folder:

update_records.sql - update 1 or more records in a table.
delete_records.sql - delete 1 or more records from a table.
db02_features.py

Create a Python script that demonstrates the ability to run sql scripts to interact with fields, update records, delete records, and maybe add additional columns.

## Perform Aggregations and queries
Implement SQL statements and queries to perform aggregations and queries.

sql_queries folder:

query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - use WHERE to filter data based on conditions.
query_sorting.sql - use ORDER BY to sort data.
query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

db03_queries.py

# Book and Author Database

## Schema Design

This project uses two related tables to store information about books and authors. The schema includes:

1. **authors**: A table containing information about authors. It includes:
   - `author_id` (Primary Key)
   - `first_name`
   - `last_name`
   - `year_born`

2. **books**: A table containing information about books. It includes:
   - `book_id` (Primary Key)
   - `title`
   - `year_published`
   - `author_id` (Foreign Key referencing `authors`)

## SQL Scripts

- `01_drop_tables.sql`: Drops the `authors` and `books` tables if they exist. This allows us to re-run the script for development or testing purposes.
- `02_create_tables.sql`: Creates the `authors` and `books` tables with the necessary schema and relationships.
- `03_insert_records.sql`: Inserts 10 records into the `authors` and `books` tables.

## Python Script

- `db01_setup.py`: This Python script demonstrates how to create the SQLite database, define the schema, and insert the records. It automatically drops existing tables to ensure a clean setup and then re-creates the schema and inserts the data.

### How to Use

1. Ensure the SQL scripts (`01_drop_tables.sql`, `02_create_tables.sql`, `03_insert_records.sql`) are located in the `sql_create` folder.
2. Run the `db01_setup.py` Python script. It will create a SQLite database (`books_authors.db`), define the tables, and insert the records.
3. The database file `books_authors.db` will be created in the project directory.

### Notes

- The schema uses a **foreign key** relationship between the `books` and `authors` tables.
- The Python script is designed to be re-runnable: it first drops any existing tables before re-creating and populating them.

### SQL Features
1. Update Records (update_records.sql)
This file contains SQL statements to update one or more records in the database. For example, updating the publication year of a book or changing an author's last name.
2. Delete Records (delete_records.sql)
This file contains SQL statements to delete records from the database. You can delete books or authors based on specific conditions.

## SQL Queries
SQL File Execution: The Python script now executes SQL files from the sql_queries folder.
Query Execution:
1. Aggregation: Queries like counting the total number of books and calculating the average publication year are executed.
2. Filtering: Books published after 2015 are filtered.
3. Sorting: Books are sorted by publication year.
4. Grouping: Books are grouped by author, showing how many books each author has published.
5. Join: The script uses INNER JOIN and LEFT JOIN to fetch books with their respective authors.
Displaying Results: The results of each query are printed to the console.
Optional: If needed, you can further enhance this script to create visualizations using matplotlib.

## Visualizations Using Matplotlib

Books Published Per Year: A bar chart displays the total number of books published each year.
Books Published Per Author: A horizontal bar chart shows how many books each author has published.