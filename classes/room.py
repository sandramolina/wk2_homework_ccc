class Room:
    def __init__(self, input_room_name):
        self.room_name = input_room_name
        self.guest_list = []
        self.playlist = []

    def add_song_to_room(self, song_to_add):
        self.playlist.append(song_to_add)