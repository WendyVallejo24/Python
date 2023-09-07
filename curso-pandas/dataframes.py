import pandas as pd

dataframe1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(dataframe1)
print('\n')
dataframe2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(dataframe2)

dataframe3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(dataframe3)

# Series
series1 = pd.Series([1, 2, 3, 4, 5])
print(series1)

series2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(series2)

# Reading data files
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews)

wine_reviews.head()

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
