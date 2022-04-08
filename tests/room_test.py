import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("The tipsy gipsy")
        self.song_to_add1 = Song("Bohemian Rhapsody", "Queen", 6)
        self.song_to_add2 = Song("Wannabe", "Spice Girls", 3)
        self.song_to_add3 = Song("Karma Police", "Radiohead", 3)
        self.song_to_add4 = Song("I wanna be yours", "Arctic Monkeys", 4)
        self.song_to_add5 = Song("Salsa y Control", "Grupo Niche", 4)
        self.song_to_add6 = Song("My Heart Will Go On", "Celine Dion", 3)

        self.guest2 = Guest("Eevee Costa", 25, 150, self.song_to_add2)
    
    def test_room_name(self):
        self.assertEqual("The tipsy gipsy", self.room1.room_name)

    def test_song_add_song_to_room(self):
        for i in range(0, 5):
            self.room1.add_song_to_room(self.song_to_add1)
        self.assertEqual(5, len(self.room1.song_list))

    def test_fav_song_say_yeah(self):
        self.room1.add_song_to_room(self.song_to_add1)
        self.room1.add_song_to_room(self.song_to_add2)
        self.room1.add_song_to_room(self.song_to_add3)
        self.room1.add_song_to_room(self.song_to_add4)
        self.room1.add_song_to_room(self.song_to_add5)
        self.room1.add_song_to_room(self.song_to_add6)
        self.assertEqual("Yeah, this is my jam!!", self.guest2.fav_song_played(self.room1))

    