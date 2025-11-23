import pandas as pd

df = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Customer": ["Arun", "Meera", "John", "Priya", "Rahul",
                 "Vikram", "Simran", "David", "Isha", "Karan"],
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor",
                "Mouse", "Printer", "Tablet", "Camera", "Speaker"],
    "Quantity": [1, 2, 1, 3, 2, 1, 1, 1, 2, 4],
    "Price": [55000, 18000, 3000, 1500, 12000,
              700, 9000, 20000, 25000, 4000]
}, index=[
    "s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"
])

print(df)

print(df.loc["s2"])
print(df.loc["s2", "Product"])
print(df.loc[["s1", "s5", "s9"]])
print(df.loc["s3":"s7"])
print(df.loc[:, ["Customer", "Price"]])

print(df.iloc[0])
print(df.iloc[[0, 3, 7]])
print(df.iloc[1, 2])
print(df.iloc[0:5])
print(df.iloc[0:5, 0:3])

