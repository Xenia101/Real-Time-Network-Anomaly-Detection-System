from sklearn.cluster import KMeans
import numpy as np
import csv

with open("output/output.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

X = np.array([x[4:] for x in data[1:]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

kmeans.predict([[0, 0], [12, 3]])

kmeans.cluster_centers_
