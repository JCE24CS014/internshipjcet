import pandas as pd
import matplotlib.pyplot as plt
table=pd.read_csv("data/disney_movies.csv")
print(table)


# Show first 5 rows
print("\nFIRST 5 ROWS OF DATASET")
print(table.head())

# Show column names
print("\nCOLUMN NAMES")
print(table.columns)

# 1. Top 10 Highest Gross Movies
print("\nTOP 10 HIGHEST GROSS MOVIES")
top_gross = table.sort_values(by='total_gross', ascending=False)
print(top_gross[['movie_title', 'total_gross']].head(10))

# 2. Top 10 Inflation Adjusted Gross Movies
print("\nTOP 10 INFLATION ADJUSTED GROSS MOVIES")
top_adjusted = table.sort_values(by='inflation_adjusted_gross', ascending=False)
print(top_adjusted[['movie_title', 'inflation_adjusted_gross']].head(10))

# 3. Number of Movies in Each Genre
print("\nNUMBER OF MOVIES IN EACH GENRE")
genre_count = table.groupby('genre').size()
print(genre_count)

# 4. Number of Movies by MPAA Rating
print("\nNUMBER OF MOVIES BY MPAA RATING")
rating_count = table.groupby('mpaa_rating').size()
print(rating_count)

# 5. Movies Released Each Year
print("\nMOVIES RELEASED EACH YEAR")

# Convert release_date to datetime
table['release_date'] = pd.to_datetime(table['release_date'])

# Extract year
table['year'] = table['release_date'].dt.year

movies_per_year = table.groupby('year').size()
print(movies_per_year)

# 6. Top 5 Adventure Movies by Gross
print("\nTOP 5 ADVENTURE MOVIES")

adventure_movies = table[table['genre'] == 'Adventure']

top_adventure = adventure_movies.sort_values(by='total_gross', ascending=False)

print(top_adventure[['movie_title', 'total_gross']].head(5))

# 7. Top 5 Comedy Movies by Gross
print("\nTOP 5 COMEDY MOVIES")

comedy_movies = table[table['genre'] == 'Comedy']

top_comedy = comedy_movies.sort_values(by='total_gross', ascending=False)

print(top_comedy[['movie_title', 'total_gross']].head(5))
genre_count = table.groupby('genre').size()

genre_count.plot(kind='bar')

plt.title("Movies in Each Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")

plt.show()