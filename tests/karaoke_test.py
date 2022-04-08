import unittest
from classes.guest import Guest

from classes.karaoke import Karaoke
from classes.room import Room


class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke1 = Karaoke("Venue 56")
        self.room1 = Room("The tipsy gipsy")
        self.guest1 = Guest("Pikachu Gutierrez", 32)
        self.guest2 = Guest("Eevee Costa", 25)
    
    def test_karoke_name(self):
        self.assertEqual("Venue 56", self.karaoke1.name)
    
    def test_add_room(self):
        self.karaoke1.add_karaoke_room(self.room1)
        self.assertEqual(1, len(self.karaoke1.room_list))

    def test_check_in_out_guest_to_room(self):
        self.karaoke1.check_in_out_guest_to_room(self.room1, self.guest1)
        self.karaoke1.check_in_out_guest_to_room(self.room1, self.guest2)
        self.assertEqual(2, len(self.room1.guest_list))
