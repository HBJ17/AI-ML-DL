import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Age": [21, 22, 23, 24],
    "Marks": [90, 85, 88, 92]
}, index=["a", "b", "c", "d"])

print(df)

print(df.loc["b"])
print(df.loc["b", "Age"])
print(df.loc[["a", "c", "d"]])