import matplotlib.pyplot as plt
# Load the data
# size of the houses in sq ft
X = [1200, 1500, 1700, 1600, 1300, 1400, 1000, 900, 800, 1100, 1200, 1300, 1600, 1900, 1800, 2000, 2100, 2200, 2300, 2400, 2500] 
# price of the houses in $
y = [500000, 600000, 700000, 550000, 580000, 600000, 550000, 480000, 450000, 510000, 550000, 600000, 650000, 710000, 690000, 750000, 800000,
850000, 900000, 950000, 1000000] 
# Plot the data
plt.scatter(X, y, color='blue')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.title('Size vs. Price of Houses')
plt.show()

#Import necessary libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Load the data
# sizes of houses (in sq. ft.)
X = [[100], [200], [300], [400], [500]] 
y = [20000, 40000, 60000, 80000, 100000]
# prices of houses
# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)
# Print the coefficients
print(model.coef_) # slope of the line
print(model.intercept_) # y-intercept of the line
# Make predictions
X_new = [[600]] # size of a new house
y_pred = model.predict(X_new) # predicted price of the new house
print(y_pred)
# Plot the data and the line of best fit
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')