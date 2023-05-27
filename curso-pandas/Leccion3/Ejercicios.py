import pandas as pd

pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Ejercicio 1
median_points = reviews.points.median()
print(median_points)

# Ejercicio 2
countries = reviews.country.unique()
print(countries)

# Ejercicio 3
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)

# Ejercicio 4
centered_price = reviews.price - reviews.price.mean()
print(centered_price)

# Ejercicio 5
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine)

# Ejercicio 6
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)

# Ejercicio 7
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)