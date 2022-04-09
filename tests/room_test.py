import unittest
from classes.bar import Bar
from classes.drinks import Drinks
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("The tipsy gipsy")

        self.bar_room1 = Bar() 

        self.song_to_add1 = Song("Bohemian Rhapsody", "Queen", 6)
        self.song_to_add2 = Song("Wannabe", "Spice Girls", 3)
        self.song_to_add3 = Song("Karma Police", "Radiohead", 3)
        self.song_to_add4 = Song("I wanna be yours", "Arctic Monkeys", 4)
        self.song_to_add5 = Song("Salsa y Control", "Grupo Niche", 4)
        self.song_to_add6 = Song("My Heart Will Go On", "Celine Dion", 3)

        self.guest2 = Guest("Eevee Costa", 25, 150, self.song_to_add2)
        self.guest7 = Guest("Squirtle Blueman", 40, 120, Song("Total Eclipse of the Heart", "Bonnie Tyler", 5))        

        self.drink1 = Drinks("Beer", 3.4)
        self.drink2 = Drinks("Cocktail", 5)
    
    def test_room_name(self):
        self.assertEqual("The tipsy gipsy", self.room1.room_name)

    def test_song_add_song_to_room(self):
        for i in range(0, 5):
            self.room1.add_song_to_room(self.song_to_add1)
        self.assertEqual(5, len(self.room1.playlist))

    def test_fav_song_say_yeah(self):
        self.room1.add_song_to_room(self.song_to_add1)
        self.room1.add_song_to_room(self.song_to_add2)
        self.room1.add_song_to_room(self.song_to_add3)
        self.room1.add_song_to_room(self.song_to_add4)
        self.room1.add_song_to_room(self.song_to_add5)
        self.room1.add_song_to_room(self.song_to_add6)
        self.assertEqual("Yeah, this is my jam!!", self.guest2.fav_song_played(self.room1))

    def test_fav_song_say_booo(self):
        self.room1.add_song_to_room(self.song_to_add1)
        self.room1.add_song_to_room(self.song_to_add2)
        self.room1.add_song_to_room(self.song_to_add3)
        self.assertEqual("Boooo", self.guest7.fav_song_played(self.room1))

    def test_bar_till(self):
        self.assertEqual(0, self.bar_room1.bar_till)

    def test_add_drinks_to_bar(self):
        self.bar_room1.add_drinks_to_bar(self.drink1, 10)
        self.assertEqual(1, len(self.bar_room1.drinks))
        self.assertEqual(10, self.drink1.stock)
    
    # def test_remove_drink_from_bar(self):
    #     for i in range(0, 5):
    #         self.bar_room1.add_drinks_to_bar(self.drink1)
        
    #     self.bar_room1.remove_drinks_to_bar(self.drink1)
    #     self.assertEqual(1, len(self.bar_room1.drinks))