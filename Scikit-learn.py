from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
pred = model.predict([[6]])
print("Prediction for input 6:", pred)
