class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls,genre):
        if cls.genres.count(genre) == 0:
            cls.genres.append(genre)
    

    @classmethod
    def add_to_artists(cls,artist):
        if cls.artists.count(artist) == 0:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count.setdefault(genre,0)
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls,artist):
        cls.artist_count.setdefault(artist,0)
        cls.artist_count[artist] += 1
