import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

summary1 = reviews.points.describe()
print(summary1)
print('\n')
summary2 =reviews.taster_name.describe()
print(summary2)
print('\n')
summary3 = reviews.points.mean()
print(summary3)
print('\n')
summary4 = reviews.taster_name.unique()
print(summary4)
print('\n')
summary5 = reviews.taster_name.value_counts()
print(summary5)
print('\n')

maps1 = review_points_mean = reviews.points.mean()
print(maps1)
print('\n')
maps2 = reviews.points.map(lambda p: p - review_points_mean)
print(maps2)
print('\n')

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

maps3 = reviews.apply(remean_points, axis='columns')
print(maps3)
maps4 = reviews.head(1)
print(maps4)

review_points_mean = reviews.points.mean()
maps5 = reviews.points - review_points_mean
print(maps5)

maps6 = reviews.country + " - " + reviews.region_1
print(maps6)