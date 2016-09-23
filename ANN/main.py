import numpy as np
import math
import matplotlib.pyplot as plt
from kmeans.k_means import KMeans

def csvImport(file_name):
	fhand = open(file_name, 'r')
	raw_data = [",".join(line.split(',')[:2]) for line in fhand]
	raw_data = [float(element) for element in ",".join(raw_data).split(",")]
	data = np.array(raw_data).reshape(math.ceil(len(raw_data) / 2), 2)

	return data

data = csvImport("iris-data.csv")

fig = plt.figure(1)
plt.subplot(211)
plt.scatter(data[:,0], data[:,1], s=50)

clusterer = KMeans(data, 3)
cluster_data = clusterer.clustering()

plt.subplot(212)
plt.scatter(data[:,0], data[:,1], c=cluster_data, s=50, cmap='rainbow')

plt.show() 