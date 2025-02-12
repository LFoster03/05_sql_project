-- delete_records.sql

-- Delete a specific book by its ID
DELETE FROM books
WHERE book_id = 10;

-- Delete an author by their author_id
DELETE FROM authors
WHERE author_id = 'F309';
