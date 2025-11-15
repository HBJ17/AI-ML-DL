import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Age": [21, 22, 23, 24],
    "Marks": [90, 85, 88, 92]
}, index=["a", "b", "c", "d"])

print(df)

# loc label based
print(df.loc["b"])
print(df.loc["b", "Age"])
print(df.loc[["a", "c", "d"]])
print(df.loc["a":"c"])
print(df.loc[:, ["Name", "Marks"]])

#iloc integer based
print(df.iloc[0])
print(df.iloc[[0, 2]])
print(df.iloc[1, 1])
print(df.iloc[0:2])
print(df.iloc[0:2, 0:2])