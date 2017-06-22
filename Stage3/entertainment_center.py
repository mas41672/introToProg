import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
"A story of a boy and his toys that come to life",
"http://www.hobbyconsolas.com/sites/hobbyconsolas.com/public/media/image"+
"/2013/10/254726-toy-story-espacio-disney-infinity.png",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
"A marine on an alien planet",
"https://vignette4.wikia.nocookie.net/jamescameronsavatar/images/6/6c/" +
"Avatar_Poster.jpg/revision/latest?cb=20100105110229",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(avatar.storyline)
avatar.show_trailer()

full_metal_jacket = media.Movie("Full Metal Jacket",
"A two-segement look at the effect fo the military mindset and war itself" +
" on Vietnam era Marines.",
"http://horrornews.net/wp-content/uploads/2010/11/Full-Metal-Jacket-1.png",
"https://www.youtube.com/watch?v=x9f6JaaX7Wg")

pulp_fiction = media.Movie("Pulp Fiction",
"The lives of two mob hit men, a boxer, a gangster's wife, and a pair of" +
" diner bandits intertwine in four tales of violence and redemption.",
"https://ih1.redbubble.net/image.87997040.6932/flat,800x800,075,f.jpg",
"https://www.youtube.com/watch?v=s7EdQ4FqbhY")

sing = media.Movie("Sing",
"In a city of humanoid animals, a hustling theater impresario's attempt to" + 
" save his theater with a singing competition becomes grander than he anticipates even as its finalists' find that their lives will never be the same.",
"http://tivolilibrary.org/wp-content/uploads/2015/04/movie_sing_poster_website.png",
"https://www.youtube.com/watch?v=FgcQpy0Rnr4")

titanic = media.Movie("Titanic",
"A seventeen-year-old aristocrat falls in love with a kind but poor artist "+ 
"aboard the luxurious, ill-fated R.M.S. Titanic.",
"http://www.bestforfilm.com/wp-content/uploads/2012/02/titanic-poster.png",
"https://www.youtube.com/watch?v=1faTu7KOoHw")

movies = [toy_story, avatar, full_metal_jacket, pulp_fiction, sing, titanic]
fresh_tomatoes.open_movies_page(movies)