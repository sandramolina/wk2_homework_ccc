import unittest

from classes.karaoke import Karaoke


class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke1 = Karaoke("Venue 56")
    
    def test_karoke_name(self):
        self.assertEqual("Venue 56", self.karaoke1.name)