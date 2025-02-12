-- query_filter.sql

-- Get all books published after the year 2015
SELECT * FROM books
WHERE year_published > 2015;

-- Get all books by a specific author (e.g., "Sally Rooney")
SELECT * FROM books
WHERE author_id = 'F306';
