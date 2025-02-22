import pandas as pd
import os

#finding path of the files
for dirname, _, filenames in os.walk('archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#combining ratings with movies into one df
ratings_file = 'archive/ratings.csv'
df_rate = pd.read_csv(ratings_file)

movies_file = 'archive/movies.csv'
df_movie = pd.read_csv(movies_file)

movie_data = pd.merge(df_rate, df_movie, on='movieId')
movie_data.drop(['timestamp', 'movieId', 'userId'], axis=1, inplace=True)

#cut down on the data to make it easier to work with
random_sample = movie_data.sample(n=500, random_state=42)
print(random_sample)
