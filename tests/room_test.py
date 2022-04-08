import unittest

from classes.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("The tipsy gipsy")
        self.song_to_add1 = "Volare"
    
    def test_room_name(self):
        self.assertEqual("The tipsy gipsy", self.room1.room_name)

    def test_song_add_song_to_room(self):
        self.room1.add_song_to_room(self.song_to_add1)
        self.assertEqual(1, len(self.room1.song_list))
