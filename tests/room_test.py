import unittest

from classes.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("The tipsy gipsy")
    
    def test_room_name(self):
        self.assertEqual("The tipsy gipsy", self.room1.room_name)