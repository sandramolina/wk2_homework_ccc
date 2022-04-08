class Room:
    def __init__(self, input_room_name):
        self.room_name = input_room_name
        self.guest_list = []
        self.song_list = []

    def add_song_to_room(self, song_to_add):
        self.song_list.append(song_to_add)