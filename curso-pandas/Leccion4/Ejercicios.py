import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Ejercicio 1
reviews_written = reviews.groupby('taster_twitter_handle').size()
print(reviews_written)


# Ejercicio 2
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)

# Ejercicio 3
price_extremes = reviews.groupby('variety').price.agg([min, max])
print(price_extremes)

# Ejercicio 4
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties)

# Ejercicio 5
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
reviewer_mean_ratings.describe()

# Ejercicio 6
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)