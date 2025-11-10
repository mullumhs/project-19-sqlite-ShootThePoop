import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create the movies table

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    year INTEGER,
    rating FLOAT
)
''')

# Insert a single movie using string formatting (UNSAFE - vulnerable to SQL injection)
movie = ('The Godfather', 'Francis Ford Coppola', 1972, 9.2)
cursor.execute(f'''
INSERT INTO movies (title, director, year, rating)
VALUES ('{movie[0]}', '{movie[1]}', {movie[2]}, {movie[3]})
''')

# Insert a single movie using a parameterized query (SAFE)

cursor.execute('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', ('Pulp Fiction', 'Quentin Tarantino', 1994, 8.9))

# List of movies to insert
movies = [
    ('The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),
    ('Inception', 'Christopher Nolan', 2010, 8.8),
    ('The Matrix', 'Lana and Lilly Wachowski', 1999, 8.7),
    ('Interstellar', 'Christopher Nolan', 2014, 8.6),
    ('Bill', "William", 2008, 5.1),
    ('Test', "Author", 5, 2.0)
]

# Insert multiple movies
cursor.executemany('''
INSERT INTO movies (title, director, year, rating)
VALUES (?, ?, ?, ?)
''', movies)

# Commit the changes and close the connection
conn.commit()
conn.close()