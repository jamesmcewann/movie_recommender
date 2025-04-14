class User:
    def __init__(self, user):
        user.id = None
        self.name = user['name']
        self.image = None
        self.watched_movies = []
        self.to_watch_movies = []


# Not sure if these should be here
    def login_success(self):
        print(f"Welcome {self.name}!")
        return True
    
    def login_failure(self):
        print("Login failed. Please try again.")
        return False
    
    def register_user(self, username, password):
        self.username = username
        self.password = password
        self.image = None
        self.watched_movies = []
        self.to_watch_movies = []
        # Save user to database or file
        
        print(f"User {self.username} registered successfully.")
    
