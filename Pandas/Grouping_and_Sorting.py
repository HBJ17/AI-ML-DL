import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("D:\Studies\Projects\Python\AI-ML-DL\data\winemag-data-130k-v2.csv", index_col=0)

reviews.groupby('points').points.count()
print(reviews)


reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
print(reviews)

reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
print(reviews)

reviews.groupby(['country']).price.agg([len, min, max])
print(reviews)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

mi = countries_reviewed.index
type(mi)

