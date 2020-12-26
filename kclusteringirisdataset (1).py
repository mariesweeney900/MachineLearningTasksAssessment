# -*- coding: utf-8 -*-
"""KClusteringIrisDataSet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vS12Epd9yiOrnBfkt4nBFrPuxrNGBkL0
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

#Loads the iris dataset
iris = datasets.load_iris()

#Adapted from https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee
#Identify x and y for the k means clustering

X = iris.data[:, :2]
y = iris.target

#Adapted from https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee
#Plot the dataset via scatterplot
#Assign the data an x and y label

plt.scatter(X[:,0], X[:,1], c=y, cmap='gist_rainbow')
plt.xlabel('Spea1 Length', fontsize=18)
plt.ylabel('Sepal Width', fontsize=18)

#Adapted from https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee
#Carry out k means fitting

km = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)
km.fit(X)

#Adapted from https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee
#The center of the cluster is the average of all points

centers = km.cluster_centers_
print(centers)

#Adapted from https://medium.com/@belen.sanchez27/predicting-iris-flower-species-with-k-means-clustering-in-python-f6e46806aaee
#Apply the labels

#The following identifies the observations belonging to each cluster.
new_labels = km.labels_
# The chosen clusters are plotted and differentiated
fig, axes = plt.subplots(1, 2, figsize=(16,8))
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow',
edgecolor='k', s=150)
axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',
edgecolor='k', s=150)
axes[0].set_xlabel('Sepal length', fontsize=18)
axes[0].set_ylabel('Sepal width', fontsize=18)
axes[1].set_xlabel('Sepal length', fontsize=18)
axes[1].set_ylabel('Sepal width', fontsize=18)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)

"""
# Adapted from https://developers.google.com/machine-learning/clustering/algorithm/advantages-disadvantages
#http://playwidtech.blogspot.com/2013/02/k-means-clustering-advantages-and.html

The distinct advantages and disadvantages of a K-Means algorithm.

Advantages:
K-Means is basic and fast to compute.
It is very predictive and visualisations are excellent at displaying results.
If the variables are large, K-Means is more efficient in calculations, than any form of hirerachical clustering 
as long as the size of the cluster remains small. 
K-means can produce a more compact cluster, as long as it retains its circular structure. 

Disadvantages:
K-Means is overly reliant on scale and is not useful for data points containing an amalgamation of differing shapes and characteristics.
The results are more subjective, peresenting problems in evaluating the findings. It demands much more human investigation than the reliablility that metrics offer.
It can be difficult to predict the k value. It can be problematice when working with an ecological problem. Commencing with stratifications that can be in anyway erratic,
may result in entirely different final clustering. If the clusters are a different size or density, it can skew the original data or a cluster.



"""