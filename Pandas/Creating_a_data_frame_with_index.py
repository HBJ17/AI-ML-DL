import pandas as pd

data = {
    'Model': ['Model-A', 'Model-B', 'Model-C', 'Model-D', 'Model-E', 'Model-F', 'Model-G', 'Model-H'],
    'Epochs': [10, 20, 15, 25, 12, 18, 30, 22],
    'Accuracy(%)': [92.4, 88.1, 94.7, 90.3, 93.5, 89.9, 95.2, 91.7],
    'Loss': [0.28, 0.34, 0.21, 0.30, 0.24, 0.33, 0.19, 0.27],
    'Inference_Time(ms)': [12.3, 15.7, 10.9, 14.2, 13.1, 16.8, 11.4, 12.9],
    'Probability_Score': [0.91, 0.88, 0.95, 0.90, 0.93, 0.89, 0.96, 0.92]
}

df = pd.DataFrame(data, index=[1,2,3,4,5,6,7,8])

print(df)

mean = df['Probability_Score'].mean()
print(f"\nAverage Probability Score: {mean:.2f}")
