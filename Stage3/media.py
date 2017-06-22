import webbrowser

class Movie():
	"""class Movie/ instantiate with: Myname.Movie(four attributes)
	   four attributes: movie title, movie stroyline, poster image and trailer
	   method: show_trailer()"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		""" show trailer method of class Movie
		    opens the browser with the given url
		    input: trailer_youtube_url [string] """
		webbrowser.open(self.trailer_youtube_url)