import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repositories as album_repositories 
import repositories.artist_repositories as artist_repositories  

album_repositories.delete_all()

album_1 = Album("Beat the Devil's Tattoo", "Rock", "BRMC")
album_repositories.save(album_1)

album_2 = Album("Grinderman 2", "Rock", "Grinderman")

res = album_repositories.select_all()
for album in res:
    print(album.__dict__)

artist_1 = Artist("BRMC")
artist_repositories.save(artist_1)

artist_2 = Artist("Grinderman")
artist_repositories.save(artist_2)

artist_repository/select_all