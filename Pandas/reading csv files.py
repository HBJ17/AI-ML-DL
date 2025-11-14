import pandas as pd

data = pd.read_csv("D:\Studies\Projects\Python\AI-ML-DL\data\chatgpt_cleaned.csv", index_col=1)

shape = data.shape
print(shape)

#exploring the data
print(data)
print()