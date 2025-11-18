import pandas as pd

stock_prices = [
    152.34, 154.10, 153.78, 156.42, 158.90, 157.25, 159.88, 161.20, 160.45, 162.33,
    164.10, 163.55, 165.78, 167.40, 166.25, 168.92, 170.10, 169.44, 171.33, 172.85,
    174.20, 173.55, 175.88, 177.40, 176.95, 178.33, 179.22, 180.10, 181.75, 182.50
]

stock_series = pd.Series(stock_prices, name="Stock_Closing_Price", index=[f"Day_{i}" for i in range(1, 31)])

print(stock_series)

