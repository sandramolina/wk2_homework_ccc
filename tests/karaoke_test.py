import unittest
from classes.guest import Guest

from classes.karaoke import Karaoke
from classes.room import Room
from classes.song import Song


class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke1 = Karaoke("Venue 56")

        self.room1 = Room("The tipsy gipsy")

        self.guest1 = Guest("Pikachu Gutierrez", 32, 100, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest2 = Guest("Eevee Costa", 25, 150, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest3 = Guest("Charizard Smith", 22, 180, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest4 = Guest("Snorlax Kardashian", 30, 160, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest5 = Guest("Charmander Onfire", 31, 125, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest6 = Guest("Squirtle Blueman", 40, 1, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest7 = Guest("Squirtle Blueman", 40, 120, Song("Bohemian Rhapsody", "Queen", 6))
    
    def test_karoke_name(self):
        self.assertEqual("Venue 56", self.karaoke1.name)
    
    def test_add_room(self):
        self.karaoke1.add_karaoke_room(self.room1)
        self.assertEqual(1, len(self.karaoke1.room_list))

    def test_entry_fee(self):
        self.assertEqual(10, self.karaoke1.entry_fee)

    def test_check_in_guest_to_room(self):
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest1)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest2)
        self.assertEqual(2, len(self.room1.guest_list))

    def test_check_in_guest_to_room_no_possible(self):
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest1)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest2)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest3)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest4)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest5)
        self.assertEqual("Room is full, please take guest to a new room", self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest7))

    def test_check_out_guest_from_room(self):
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest1)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest2)
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest3)
        self.karaoke1.check_out_guest_from_room(self.room1, self.guest1)
        self.assertEqual(2, len(self.room1.guest_list))

    def test_charge_karaoke_fee(self):
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest1)
        self.assertEqual(90, self.guest1.wallet)

    def test_till_increase(self):
        self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest1)
        self.assertEqual(10, self.karaoke1.till)

    def test_can_afford_entry_fee_true(self):
        self.assertEqual(True, self.guest1.can_afford_entry_fee(self.karaoke1))

    def test_can_afford_entry_fee_false(self):
        self.assertEqual(False, self.guest6.can_afford_entry_fee(self.karaoke1))

    def test_guest_cannot_afford_entry_fee_so_no_check_in(self):
        self.assertEqual("Guest has no sufficient funds", self.karaoke1.check_in_guest_to_room(self.karaoke1, self.room1, self.guest6))