class Karaoke:
    def __init__(self, input_name):
        self.name = input_name
        self.room_list = []
    
    def add_karaoke_room(self, room_to_add):
        self.room_list.append(room_to_add)