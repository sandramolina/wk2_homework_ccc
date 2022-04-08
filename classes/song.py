class Song:
    def __init__(self, input_song_name, input_artist, input_lenght):
        self.song_name = input_song_name
        self.artist = input_artist
        self.length = input_lenght
        self.song_popularity = 0 #later, create a function where the popularity increases every time someone play a certain song or maybe we can have a ramdon stars generator where everytime the song is played it assignes a value from 0-5