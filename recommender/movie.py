class Movie:
    def __init__(self, movie):
        self.image = movie['Poster_Link']
        self.title = movie['Series_Title']
        self.genre = movie['Genre']
        self.director = movie['Director']
        self.year = movie['Released_Year']
        self.imdb_rating = movie['IMDB_Rating']
        self.user_rating = 0
        self.watched = False
        self.to_watch = False

    def update_rating(self, rating):
        if rating > 5 or rating < 0:
            raise ValueError("Rating must be between 0 and 5")
        else:
            self.user_rating = rating
    
    def update_watched(self):
        if self.watched:
            self.watched = False
        else:
            self.watched = True
    
    def update_to_watch(self):
        if self.to_watch or self.watched:
            self.to_watch = False
        else:
            self.to_watch = True

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}, directed by {self.director}, Rating: {self.rating}/10, User Rating: {self.user_rating}/5"