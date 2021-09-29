import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Meatloaf")
artist_repository.save(artist_1)

artist_2 = Artist("Madonna")
artist_repository.save(artist_2)

album_1 = Album("Bat Out of Hell", "rock", artist_1)
album_repository.save(album_1)

album_2 = Album("Dead Ringer", "rock", artist_1)
album_repository.save(album_2)

album_3 = Album("True Blue", "pop", artist_2)
album_repository.save(album_3)

artist_1.name = "Queen"
artist_repository.update(artist_1)

pdb.set_trace()