#Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
# Load the data
X = [['red', 'round', 10], ['green', 'oval', 5], ['orange', 'round', 7],
['yellow', 'oval', 3], ['red', 'oval', 5], ['green', 'round', 4]]
# fruit features
y = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [1,0,0], [0, 1, 0]]
# fruit types (encoded)
# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)
# Make predictions
X_new = [['orange', 'round', 8]] # features of a new fruit
y_pred = model.predict(X_new)
# predicted type of the new fruit
# Decode the predicted type
fruit_types = ['apple', 'pear', 'orange']
predicted_type = fruit_types [np.argmax(y_pred)]
print(predicted_type)
