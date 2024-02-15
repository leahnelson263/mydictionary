#Create a dictionary named movie-ratings with at least five movies as keys and their ratings (out of 10) as values. 
#Ask the user for a movie title. Write a function named recommend_movie that takes the movie_rating dictionary 
#and the movie title as arguments. The function should check if the movie is in the dictionary and recommend 
#the movie if it has a rating of 8 or higher. Otherwise, suggest movie titles that have a rating of 8 or higher. 
#If the movie is not found in the dictionary, it should still recommend movies that are rated 8 or higher.
print()
movie_rating = {"The Notebook": 8, "Captain America": 7, "Cars": 9, "Titanic": 6, "Confessions of a Shopaholic": 9}
ux_movie = input("Enter a movie title: ").title()

def main():
    recommend_movie(movie_rating, ux_movie)


def recommend_movie(movie_rating, ux_movie):
    if ux_movie in movie_rating and movie_rating[ux_movie] >= 8:
        print(f">>> {ux_movie} is recommended!! This movie has a rating of {movie_rating[ux_movie]}.\n")
    else:
        print()
        print("Movie Recommendations:")
        for movie, rating in movie_rating.items():
            if rating <= 8:
                print(f"{movie} has a rating of {rating}.")

main()