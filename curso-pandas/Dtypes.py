import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

data1 = reviews.price.dtype
print(data1)

data2 = reviews.dtypes
print(data2)

data3 = reviews.points.astype('float64')
print(data3)

data4 = reviews.index.dtype
print(data4)

# Missing data
missing1 = reviews[pd.isnull(reviews.country)]
print(missing1)

missing2 = reviews.region_2.fillna("Unknown")
print(missing2)

missing3 = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(missing3)
