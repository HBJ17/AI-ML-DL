import pandas as pd
data = pd.read_csv("D:\Studies\Projects\Python\AI-ML-DL\data\chatgpt_cleaned.csv", index_col=0)
print(data.head())
print()
print(data.info())
print()
print(data.describe())
print(data.shape)


