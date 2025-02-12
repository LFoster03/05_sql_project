-- update_records.sql

-- Update the year published for a specific book
UPDATE books
SET year_published = 2021
WHERE book_id = 7;

-- Update author's last name
UPDATE authors
SET last_name = 'Bennett'
WHERE author_id = 'F305';
