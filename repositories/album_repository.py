from pdb import run
from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING * "
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row["artist_id"])
        album = Album(row["title"], row["genre"], artist)
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["title"], result["genre"], artist)
    return album

def delete(id):
    sql = "DELETE FROM albums WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE ID = %s"
    values = (album.title, album.genre, album.artist.id, album.id)
    run_sql(sql, values)



