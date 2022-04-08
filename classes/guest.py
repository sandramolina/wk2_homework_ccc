class Guest:
    def __init__(self, input_name, input_age, input_wallet):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
    
    def can_afford_entry_fee(self, karaoke):
        return self.wallet >= karaoke.entry_fee