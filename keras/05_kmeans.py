#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# import sci-kit learn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

# 입력 data 정의
df = np.array([[1,4],[2,2],[2,5],[3,3],[3,4],[4,7],[5,6],[6,4],[6,7],[7,6],[7,9],[8,7],[8,9],[9,4],[9,8]])
print ('Input data:')
print (df)

# cluster 개수 정의
n_clusters = 3

# K-mean 알고리즘 적용
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10)

# k-mean cluster결과 
y_pred = kmeans.fit_predict(df)


# The silhouette_score gives the average value for all the samples.
# This gives a perspective into the density and separation of the formed clusters
# https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
silhouette_avg = silhouette_score(df, y_pred)

# Compute the silhouette scores for each sample
sample_silhouette_values = silhouette_samples(df, y_pred)

print ('clusters:')
print (y_pred)

print ('kmeans.inertia:',kmeans.inertia_)
print ('kmeans.labels:',kmeans.labels_)
print ('kmeans.algorithm:',kmeans.algorithm)

# select # of cluster
print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg)
print ('sample_silhouette_values:\n', sample_silhouette_values)

# plot
plt.scatter(df[:,0], df[:,1])
plt.savefig('05_kmeans_original.png')
plt.clf()

plt.scatter(df[:,0], df[:,1], c=y_pred)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red')
plt.savefig('05_kmeans_centers.png')


