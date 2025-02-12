-- query_join.sql

-- Get a list of books along with the author's full name (using INNER JOIN)
SELECT books.title, books.year_published, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Get a list of books with the author's name, including books with no authors (using LEFT JOIN)
SELECT books.title, books.year_published, authors.first_name, authors.last_name
FROM books
LEFT JOIN authors ON books.author_id = authors.author_id;
