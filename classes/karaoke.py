class Karaoke:
    def __init__(self, input_name):
        self.name = input_name
        self.room_list = []
        self.till = 0
        self.entry_fee = 10
    
    def add_karaoke_room(self, room_to_add):
        self.room_list.append(room_to_add)
    
    def check_in_guest_to_room(self, karaoke, room, guest_to_add):
        if guest_to_add.can_afford_entry_fee(karaoke):
            if len(room.guest_list) >= 5:
                return "Room is full, please take guest to a new room"
            else:
                room.guest_list.append(guest_to_add)
                guest_to_add.wallet -= self.entry_fee
                karaoke.till += self.entry_fee
        else:
            return "Guest has no sufficient funds"

    def check_out_guest_from_room(self, room, guest_to_remove):
        room.guest_list.remove(guest_to_remove)