import pandas as pd

# Create DataFrame
data = {'Name': ['Asha', 'Bala', 'Catherine'],
        'Age': [20, 22, 19],
        'Score': [88, 92, 95]}
df = pd.DataFrame(data)

print(df)
print("\nAverage Score:", df['Score'].mean())
