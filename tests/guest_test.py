import unittest

from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Pikachu Gutierrez", 32)
        self.guest2 = Guest("Eevee Costa", 25)
    
    def test_guest_name(self):
        self.assertEqual("Pikachu Gutierrez", self.guest1.name)
    
    def test_guest_age(self):
        self.assertEqual(25, self.guest2.age)
