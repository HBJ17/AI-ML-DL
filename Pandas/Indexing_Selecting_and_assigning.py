#to directly install the dataset from kaggle
'''
import kagglehub

path = kagglehub.dataset_download("manusmitajha/countrydatacsv")

print("Path to dataset files:", "D:\Studies\Projects\Python\AI-ML-DL\data")

'''
import pandas as pd

reviews = pd.read_csv("D:\Studies\Projects\Python\AI-ML-DL\data\winemag-data-130k-v2.csv", index_col=0)

pd.set_option('display.max_rows', 5)
#seeing each columns of a dataset (csv file)

print(reviews)

print(reviews.country)

print(reviews['country'])

print(reviews['country'][0])

#indexing
