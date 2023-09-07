import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Renaming
renaming1 = reviews.rename(columns={'points': 'score'})
print(renaming1)    

renaming2 = reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(renaming2)

renaming3 = reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(renaming3)

# Combining
canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

concatenar = pd.concat([canadian_youtube, british_youtube])
print(concatenar)

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

join1 = left.join(right, lsuffix='_CAN', rsuffix='_UK')
