import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Groupwise analysis
group1 = reviews.groupby('points').points.count()
print(group1)

group2 = reviews.groupby('points').price.min()
print(group2)

group3 = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
print(group3)

group4 = reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
print(group4)

#group5 = reviews.groupby(['country']).price.agg([len, min, max])
#print(group5)

# Multi-indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

mi = countries_reviewed.index
type(mi)
print(mi)

multi1 = countries_reviewed.reset_index
print(multi1)

# Sorting
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed)
sorting1 = countries_reviewed.sort_values(by='len')
print(sorting1)

sorting2 = countries_reviewed.sort_values(by='len', ascending=False)
print(sorting2)

sorting3 = countries_reviewed.sort_index()
print(sorting3)

sorting4 = countries_reviewed.sort_values(by=['country', 'len'])
print(sorting4)

