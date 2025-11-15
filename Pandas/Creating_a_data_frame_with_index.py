import pandas as pd

data = {'Name': ['Asha', 'Bala', 'Catherine'],
        'Age': [20, 22, 19],
        'Score': [88, 92, 95]}
df = pd.DataFrame(data , index = [1,2,3])

print(df)
mean = df['Score'].mean()
print(f"\nAverage Score: {mean:.2f}")

