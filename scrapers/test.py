import pandas as pd 

movies = pd.read_csv("../source/movie_metadata.csv")

movies = movies.rename(columns={"color": "COULOR", "director_name": "director"})
movies = movies.drop(columns=['num_critic_for_reviews', 'duration'])
#movies["COULOR"].fillna("No Coulor", inplace = True)
movies.fillna("No Coulor", inplace = True)
cols = movies.columns.tolist()
#print(cols)
#put this in front and then everything else
#movies = movies[ ['content_rating', 'language'] + [ col for col in movies.columns if col != 'content_rating' and col != 'language'] ]
movies = movies[['content_rating', 'language']]

print(movies.head())
#movies.to_csv(r"../output/test_movie.csv", header = True, index = False)
#print("success")