import pandas as pd

data = pd.read_csv("D:\Studies\Projects\Python\AI-ML-DL\data\car data.csv", index_col=1)

shape = data.shape
print(shape)

#exploring the data
print(data)
print()