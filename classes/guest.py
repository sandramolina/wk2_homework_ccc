class Guest:
    def __init__(self, input_name, input_age, input_wallet, input_fav_song):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.fav_song = input_fav_song
    
    def can_afford_entry_fee(self, karaoke):
        return self.wallet >= karaoke.entry_fee
    
    def fav_song_played(self, room):
        quote = "Boooo"
        for song in room.playlist:
            if song == self.fav_song:
                quote = "Yeah, this is my jam!!"
        return quote