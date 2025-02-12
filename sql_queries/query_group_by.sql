-- query_group_by.sql

-- Group books by author and count how many books each author has published
SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS total_books
FROM authors
JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id
ORDER BY total_books DESC;
