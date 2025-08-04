import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# connect to the database
db_path = "mubi_movies_ratings.db"
connection = sqlite3.connect(db_path)

# fetch the first movie record
query_first = "SELECT * FROM movies LIMIT 1;"
first_row_df = pd.read_sql_query(query_first, connection)

# exercise 3: best rated movies and filtering by release year >= 2018
query_best_rated = """SELECT movie_title, movie_release_year
FROM movies
ORDER BY movie_popularity DESC;"""
best_rated_df = pd.read_sql_query(query_best_rated, connection)
df_new = best_rated_df[best_rated_df["movie_release_year"] >= 2018]
year_counts = df_new["movie_release_year"].value_counts().sort_index()
print(year_counts)

# exercise 4: high rated movies and visualization
query_high_ratings = """SELECT movie_title, movie_release_year, rating
FROM movies
ORDER BY movie_popularity DESC;"""
high_ratings_df = pd.read_sql_query(query_high_ratings, connection)
high_ratings_df = high_ratings_df[high_ratings_df["rating"] > 4.5]
high_ratings_per_year = (
    high_ratings_df[high_ratings_df["movie_release_year"] >= 1950]
    .groupby("movie_release_year")
    .size()
)
plt.figure(figsize=(12, 6))
high_ratings_per_year.plot(kind="bar")
plt.title("Number of Movies with High Ratings per Year (1940-2023)")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# exercise 5: top directors by popularity
query_directors = """SELECT director_name, rating, movie_popularity
FROM movies
ORDER BY movie_popularity DESC
LIMIT 10;"""
directors_df = pd.read_sql_query(query_directors, connection)
plt.figure(figsize=(10, 6))
sns.barplot(data=directors_df, y="director_name", x="movie_popularity", hue="director_name")
plt.title("Top 10 Directors by Movie Popularity")
plt.xlabel("Movie Popularity")
plt.ylabel("Director")
plt.tight_layout()
plt.show()

# exercise 6: top critiques and word cloud
query_likes = """SELECT movie_id, critique, critique_likes
FROM ratings
ORDER BY critique_likes DESC
LIMIT 50;"""
likes_df = pd.read_sql_query(query_likes, connection)
print(f"\nnumber of rows: {len(likes_df)}\n")
likes_df.head()
text = " ".join(likes_df["critique"].dropna().str.lower().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="magma").generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Top 10 Most Liked critiques")
plt.show()

# cleanup
connection.close()
