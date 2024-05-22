# import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import matplotlib as mpl

# Load the data from CSV
try:
    dataFrame = pd.read_csv('D:\\University\\Programming\\Python\\Machine Learning\\Regression\\house.csv')
except FileNotFoundError:
    print("The file 'house.csv' was not found. Please check the file path.")
    exit()

# Display the DataFrame
print(dataFrame)

# Plot the data
plt.plot(dataFrame['area'], dataFrame['price'], color='red', marker='o', linestyle='dashed')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

# Prepare the data for the model
newDataFrame = dataFrame.drop('price', axis='columns')
print(newDataFrame)
price = dataFrame['price']
print(price)

# Create and train the linear regression model
reg = linear_model.LinearRegression()
reg.fit(newDataFrame, price)

# Predict the price for a given area
inputNum = int(input("Enter the area to predict the price: "))
predictedPrice = reg.predict([[inputNum]])
print("Predicted price for area ", inputNum, ":", predictedPrice)
print("Regression coefficient:", reg.coef_)
print("Regression intercept:", reg.intercept_)