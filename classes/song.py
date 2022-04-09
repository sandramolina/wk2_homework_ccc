class Song:
    def __init__(self, input_song_name, input_artist, input_lenght):
        self.song_name = input_song_name
        self.artist = input_artist
        self.length = input_lenght
        self.song_popularity = 0 #the popularity increases every time the song is played