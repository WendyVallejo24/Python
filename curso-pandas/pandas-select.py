import pandas as pd

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# select top 1 country from wine_reviews
wine_reviews_country = wine_reviews.loc[0, 'country']
print(wine_reviews_country)

# select taster_name, taster_twitter_handle, points from wine_reviews
wine_reviews_2 = wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]  
print(wine_reviews_2)

# set title as index
wine_reviews_3 = wine_reviews.set_index("title")
print(wine_reviews_3)

# select isItaly(country) from wines -- TSQL
wine_italy = wine_reviews.country == 'Italy'
print(wine_italy)

# select * from wines where country = 'Italy'
wines_all_italy = wine_reviews.loc[wine_reviews.country == 'Italy']
print(wines_all_italy)

# select * from wines where country = 'Italy' and points >= 90
wines_italy_points = wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90), ['country', 'points']]
print(wines_italy_points)

# select * from wines where country = 'Italy' or points >= 90
wines_italy_or_points = wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90), ['country', 'points']]
print(wines_italy_or_points)

# select * from wines where country in ('Italy', 'country')
wines_in_country = wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France']), ['country', 'points']]
print(wines_in_country)

# select * from wines where country not in ('Italy', 'country')
wines_not_in_country = wine_reviews.loc[~wine_reviews.country.isin(['Italy', 'France']), ['country', 'points']]
print(wines_not_in_country)

# update set point=0 wines
wines_in_country['points'] = 0
print(wines_in_country)

wines_not_in_country['points'] = range(0, len(wines_not_in_country), 1)
print(wines_not_in_country)