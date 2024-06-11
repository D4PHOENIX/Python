import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the data from CSV
try:
    dataFrame = pd.read_csv('D:\\University\\Programming\\Python\\Machine Learning\\K Means Clustering\\student_clustering.csv')
except FileNotFoundError:
    print("The file 'student_clustering.csv' was not found. Please check the file path.")
    exit()

# Display the first few rows of the DataFrame and the shape of the DataFrame
print("The shape of DataFrame is", dataFrame.shape)
print(dataFrame.head())

# Scatter plot of the data
plt.scatter(dataFrame['cgpa'], dataFrame['iq'])
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('Scatter plot of CGPA vs IQ')
plt.show()

# Prepare the data for KMeans clustering
X = dataFrame[['cgpa', 'iq']].values
# X = dataFrame.iloc[:,:]

# Apply KMeans clustering
km = KMeans(n_clusters=4, random_state=42)
yMeans = km.fit_predict(X)

# Plot the clusters
plt.scatter(X[yMeans == 0, 0], X[yMeans == 0, 1], color='red', marker='o', s=20, label='Cluster 1')
plt.scatter(X[yMeans == 1, 0], X[yMeans == 1, 1], color='blue', marker='o', s=20, label='Cluster 2')
plt.scatter(X[yMeans == 2, 0], X[yMeans == 2, 1], color='green', marker='o', s=20, label='Cluster 3')
plt.scatter(X[yMeans == 3, 0], X[yMeans == 3, 1], color='cyan', marker='o', s=20, label='Cluster 4')

# Plot the centroids
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='black', marker='+', s=100, label='Centroids')

# Label the axes and title
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('Clusters of Students')
plt.legend()
plt.show()


# Display the data points for one of the clusters
print("Data points in cluster 4:")
print(X[yMeans == 3])