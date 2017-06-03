import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc" )

#print(toy_story.storyline)

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                        "https://youtu.be/d96cjJhvlMA")

#print(guardians.storyline)
#guardians.show_trailer()

cloud_atlas = media.Movie("Cloud Atlas",
                          "An exploration of how the actions of individual lives impact one another in the past, present and future, as one soul is shaped from a killer into a hero, and an act of kindness ripples across centuries to inspire a revolution.",
                          "https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg",
                          "https://youtu.be/hWnAqFyaQ5s")

#print(cloud_atlas.title)
#print(cloud_atlas.storyline)
#cloud_atlas.show_trailer()

atlantis = media.Movie("Atlantis: The Lost Empire",
                          "A young adventurer named Milo Thatch joins an intrepid group of explorers to find the mysterious lost continent of Atlantis.",
                          "https://upload.wikimedia.org/wikipedia/en/d/de/Atlantis_The_Lost_Empire_poster.jpg",
                          "https://youtu.be/DeOo19iAJ1E")

avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron",
                          "When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's mightiest heroes to stop the villainous Ultron from enacting his terrible plan.",
                          "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                          "https://youtu.be/tmeOjFno6Do")

deadpool = media.Movie("Deadpool",
                          "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                          "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                          "https://www.youtube.com/watch?v=FyKWUTwSYAs")

goodfellas = media.Movie("Goodfellas",
                          "The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVitto in the Italian-American crime syndicate.",
                          "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                          "https://youtu.be/2ilzidi_J8Q")

movies = [toy_story, guardians, cloud_atlas, atlantis, avengers_age_of_ultron, deadpool, goodfellas]
                                     
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
