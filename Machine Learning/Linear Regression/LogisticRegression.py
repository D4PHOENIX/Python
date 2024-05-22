import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the data from CSV
try:
    dataFrame = pd.read_csv("D:\\University\\Programming\\Python\\Machine Learning\\Linear Regression\\insurance_data.csv")
except FileNotFoundError:
    print("The file 'insurance_data.csv' was not found. Please check the file path.")
    exit()

# Display the first few rows of the DataFrame
print(dataFrame.head())

# Plot the data
plt.scatter(dataFrame['age'], dataFrame['bought_insurance'], marker='o', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
plt.show()

# Split the data into training and testing sets
xTrain, xTest, yTrain, yTest = train_test_split(dataFrame[['age']], dataFrame['bought_insurance'], train_size=0.8)
print("xTest:\n", xTest)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(xTrain, yTrain)

# Make predictions
yPredicted = model.predict(xTest)
print("Predicted values:\n", yPredicted)

# Probability predictions
print("Predicted probabilities:\n", model.predict_proba(xTest))

# Model accuracy
print("Model accuracy score:\n", model.score(xTest, yTest))

# Prediction for a specific age
inputNum = int(input("Enter the age to predict if the person bought insurance: "))
predictedValue = model.predict([[inputNum]])
print("Predicted value for age ", inputNum, ":\n", predictedValue)
