import sqlite3
import random

def by_tag(tag):
    conn = sqlite3.connect('/opt/million_song/artist_term.db')
    query = f"SELECT artist_id FROM artist_term WHERE term='{tag}'"
    result = conn.execute(query)
    results = result.fetchall() # <-- many results
    term = random.choice(results)[0]
    return term

def by_artist_id(id):
    conn = sqlite3.connect('/opt/million_song/track_metadata.db')
    query = f"SELECT artist_name, title FROM songs WHERE artist_id='{id}'"
    result = conn.execute(query)
    return result.fetchall()
