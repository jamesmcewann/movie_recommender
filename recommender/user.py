class User:
    def __init__(self, user):
        user.id = None
        self.name = user['name']
        self.image = None
        self.watched_movies = []
        self.to_watch_movies = []

    def login(self):
        print(f"Welcome {self.name}!")
        return True