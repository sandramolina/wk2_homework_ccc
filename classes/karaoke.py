class Karaoke:
    def __init__(self, input_name):
        self.name = input_name
        self.room_list = []
    
    def add_karaoke_room(self, room_to_add):
        self.room_list.append(room_to_add)
    
    def check_in_guest_to_room(self, room, guest_to_add):
        room.guest_list.append(guest_to_add)
    
    def check_out_guest_from_room(self, room, guest_to_remove):
        room.guest_list.remove(guest_to_remove)