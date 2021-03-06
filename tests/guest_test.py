import unittest
from classes.drinks import Drinks

from classes.guest import Guest
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Pikachu Gutierrez", 32, 100, Song("Bohemian Rhapsody", "Queen", 6))
        self.guest2 = Guest("Eevee Costa", 25, 150, Song("Wannabe", "Spice Girls", 3))

        self.drink1 = Drinks("Beer", 3.4)
        self.drink2 = Drinks("Cocktail", 5)
        
    def test_guest_name(self):
        self.assertEqual("Pikachu Gutierrez", self.guest1.name)
    
    def test_guest_age(self):
        self.assertEqual(25, self.guest2.age)

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest1.wallet)

    def test_quest_fav_song(self):
        self.assertEqual("Wannabe", self.guest2.fav_song.song_name)
    
    def test_buy_drink(self):
        self.guest1.buy_drink(self.drink1, 2)
        self.assertEqual(93.2, self.guest1.wallet)