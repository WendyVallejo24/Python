import pandas as pd

# Ejercicio 1
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
desc = reviews['description']

# Ejercicio 2
first_desc = reviews.description.iloc[0]
print(first_desc)

# Ejercicio 3
first_row = first_row = reviews.iloc[0]
print(first_row)

# Ejercicio 4
first_descriptions = reviews.description.iloc[:10]
print(first_descriptions)

# Ejercicio 5
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]
print(sample_reviews)

# Ejercicio 6
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
print(df)

# Ejercicio 7
cols = ['country', 'variety']
df = reviews.loc[:99, cols]
print(df)

# Ejercicio 8
italian_wines = reviews[reviews.country == 'Italy']

# Ejercicio 9
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
print(top_oceania_wines)