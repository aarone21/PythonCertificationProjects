import sqlite3


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album; 
    DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    artist_id INTEGER,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
                  
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    track_id INTEGER,
    artist_id INTEGER,
    album_id INTEGER
);

''' )

handle = open('tracks.csv')
for line in handle:
    line = line.strip()
    cat = line.split(',')
    track = cat[0]
    artist = cat[1]
    album = cat[2]
    count =cat[3]
    rating = cat[4]
    length = cat[5]
    genre = cat[6]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

  

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (
                name, artist_id, album_id) VALUES (?, ?, ?)''', (genre, artist_id, album_id))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, artist_id, album_id, len, rating, count, genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ?, ?)''', 
        ( track, artist_id, album_id, length, rating, count, genre_id ) )
    cur.execute('SELECT id FROM Track WHERE title = ? ', (track, ))
    track_id = cur.fetchone()[0]
    
    
    conn.commit()