from movie import Movie

class MovieLibrary:
    def __init__(self):
        """Initialize the movie library with an empty collection."""
        self.movies = []

    def add_movie(self, movie):
        """
        Add a movie to the library.
        """
        self.movies.append(movie)

    def list_movies(self):
        for movie in self.movies:
            print(movie.title)

    def search_movies(self, search_term):
        for movie in self.movies:
            if search_term.lower() in movie.title.lower():
                return(movie.title)
            else:
                return("No movies found with that title.")
        

