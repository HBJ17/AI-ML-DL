from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# sizes of houses (sq ft)
X = np.array([1200, 1500, 1700, 1600, 1300, 1400, 1000, 900, 800, 1100, 1200, 1300, 1600, 1900, 1800, 2000, 2100, 2200, 2300, 2400, 2500]).reshape(-1, 1)

# prices
y = np.array([500000, 600000, 700000, 550000, 580000, 600000, 550000, 480000, 450000, 510000, 550000, 600000, 650000, 710000, 690000, 750000, 800000, 850000, 900000, 950000, 1000000])

# Model
model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

# Prediction
X_new = np.array([[1500]])
y_pred = model.predict(X_new)
print("Predicted Price:", y_pred)

# Plot the data and the line of best fit
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.plot(X_new, y_pred, )
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression for x and y Values')
plt.show()


