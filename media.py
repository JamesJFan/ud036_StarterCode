import webbrowser


class Movie:
    """This class is used to store movie related information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # self doesn't have to be self, but it is a convention that is used
    # constructor for class Movie, and the arguments that it takes
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # this function/method will open a trailer for a movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

