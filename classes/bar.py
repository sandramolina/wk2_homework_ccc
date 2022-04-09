class Bar:
    def __init__(self):
        self.drinks = []
        self.bar_till = 0

    def add_drinks_to_bar(self, drink_to_add, units_to_add):
        self.drinks.append(drink_to_add)
        drink_to_add.stock = units_to_add

