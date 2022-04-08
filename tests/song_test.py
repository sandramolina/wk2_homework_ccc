import unittest

from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Bohemian Rhapsody", "Queen", 6)
    
    def test_song_name(self):
        self.assertEqual("Bohemian Rhapsody", self.song1.song_name)

    def test_song_artist(self):
        self.assertEqual("Queen", self.song1.artist)

    def test_song_length(self):
        self.assertEqual(6, self.song1.length)