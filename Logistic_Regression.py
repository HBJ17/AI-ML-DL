import matplotlib.pyplot as plt
# Load the data
X = [[10, 50], [5, 40], [15, 60], [20, 65], [12, 55], [8, 35], [18, 75], [12, 45], [23, 85], [15, 55]] # customer behavior variables (number of purchases and average purchase amount)
y= [0, 1, 0, 0, 1, 0, 0, 1, 0, 1] # customer churn outcome ( = not churned, 1 churned)
# Access the first and second columns of the list X
X1= [row[0] for row in X] # first column of X
X2= [row [1] for row in X] # second column of X
# Plot the data
plt.scatter(X1, X2, c=y, cmap='coolwarm')
plt.xlabel('Number of purchases')
plt.ylabel('Average purchase amount')
plt.title('Customer behavior vs. churn outcome')
plt.show()

#Import necessary libraries
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
# Load the data
X = [[10, 5, 2], [7, 3, 1], [5, 2, 1], [3, 1, 0], [1,0,0]] #behavior variables
y = [1, 1, 0, 0, 0] # churn outcome (1 = churned, 0 = did not churn)
# Fit a logistic regression model
model = LogisticRegression()
model.fit(X, y)
# Print the coefficients
print(model.coef_)
# coefficients of the logistic function
print(model.intercept_)
# y-intercept of the logistic function
# Make predictions
X_new = [[8, 4, 2]]
# behavior variables of a new customer
y_pred = model.predict_proba(X_new) # predicted probability ofchurning
print(y_pred)
# Plot the data and the logistic regression curve
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict_proba(X) [:, 1], color='red')
