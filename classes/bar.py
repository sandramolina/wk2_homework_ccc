class Bar:
    def __init__(self):
        self.drinks = []
        self.bar_till = 0

    def add_drinks_to_bar(self, drink_to_add, units_to_add): 
        if drink_to_add not in self.drinks:
            self.drinks.append(drink_to_add)   
            drink_to_add.stock += units_to_add         
        else:       
            drink_to_add.stock += units_to_add

    def remove_drinks_from_bar(self, drink_to_remove, units_to_remove):
        self.drinks.remove(drink_to_remove)
        drink_to_remove.stock -= units_to_remove

    def sell_drinks(self, drink_to_sell, units_to_sell):
        if drink_to_sell.stock != 0:
            self.remove_drinks_from_bar(drink_to_sell, units_to_sell)
            self.bar_till += drink_to_sell.price * units_to_sell
        else: 
            return "Sorry, we don't have any left"