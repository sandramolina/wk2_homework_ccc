class Karaoke:
    def __init__(self, input_name):
        self.name = input_name
        self.room_list = []
    
    def add_karaoke_room(self, room_to_add):
        self.room_list.append(room_to_add)
    
    def check_in_guest_to_room(self, room, guest_to_add):
        if len(room.guest_list) >= 5:
            return "Room is full, please take guest to a new room"
        else:
            room.guest_list.append(guest_to_add)
            guest_to_add.wallet -= 10
    
    def check_out_guest_from_room(self, room, guest_to_remove):
        room.guest_list.remove(guest_to_remove)