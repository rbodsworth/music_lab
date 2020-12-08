import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("Beat the Devil's Tattoo", "Rock", "BRMC")

    def test_album_has_title(self):
        self.assertEqual("Beat the Devil's Tattoo", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("BRMC", self.album.artist)
        
        