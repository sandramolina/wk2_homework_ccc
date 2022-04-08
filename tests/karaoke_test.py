import unittest

from classes.karaoke import Karaoke
from classes.room import Room


class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke1 = Karaoke("Venue 56")
        self.room1 = Room("The tipsy gipsy")
    
    def test_karoke_name(self):
        self.assertEqual("Venue 56", self.karaoke1.name)
    
    def test_add_room(self):
        self.karaoke1.add_karaoke_room(self.room1)
        self.assertEqual(1, len(self.karaoke1.room_list))