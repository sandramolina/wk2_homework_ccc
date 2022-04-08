import unittest

from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("The tipsy gipsy")
        self.song_to_add1 = Song("Bohemian Rhapsody", "Queen", 6)
        self.song_to_add2 = Song("Wannabe", "Spice Girls", 3)
    
    def test_room_name(self):
        self.assertEqual("The tipsy gipsy", self.room1.room_name)

    def test_song_add_song_to_room(self):
        for i in range(0, 5):
            self.room1.add_song_to_room(self.song_to_add1)
        self.assertEqual(5, len(self.room1.song_list))
