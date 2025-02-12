-- query_sorting.sql

-- Get all books sorted by the year of publication (ascending)
SELECT * FROM books
ORDER BY year_published ASC;

-- Get all books sorted by title in descending order
SELECT * FROM books
ORDER BY title DESC;
