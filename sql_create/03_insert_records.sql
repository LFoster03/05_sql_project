
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
    