
# List of Ghibli movies
ghibli_movies = ["Spirited Away", "My Neighbor Totoro", "Princess Mononoke"]

# Print the initial list of movies
def main():
    print("Initial list of movies: ", ghibli_movies)
    # Ask the user for a movie title to add
    movie_title = input("Enter a Ghibli movie title to add: ")
    add_movie(movie_title)

    # Print the list of movies after adding
    print("List of movies after adding: ", ghibli_movies)

    # Ask the user for a movie title to remove
    movie_title = input("Enter a Ghibli movie title to remove: ")
    if movie_title in ghibli_movies:
        remove_movie(movie_title)
    else:
        print("Movie not found in the list.")

    # Print the list of movies after removing
    print("List of movies after removing: ", ghibli_movies)
    
# TO IMPLEMENT
def add_movie():
    # IMPLEMENT
    pass

def remove_movie(movie_title):
    # IMPLEMENT
    pass

main()