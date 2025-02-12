-- query_aggregation.sql

-- Count the total number of books in the database
SELECT COUNT(*) AS total_books FROM books;

-- Calculate the average year of publication for all books
SELECT AVG(year_published) AS avg_publication_year FROM books;

-- Calculate the total number of books published each year
SELECT year_published, COUNT(*) AS total_books_per_year
FROM books
GROUP BY year_published
ORDER BY year_published DESC;
