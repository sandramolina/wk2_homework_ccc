import unittest

from classes.drinks import Drinks


class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drinks("Beer", 3.4)
        self.drink2 = Drinks("Cocktail", 5)

    def test_drink_name(self):
        self.assertEqual("Beer", self.drink1.name)