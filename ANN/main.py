import numpy as np
import math
import matplotlib.pyplot as plt
from kmeans.k_means import KMeans


def vectorMod(array):
    """
    @Info: Returns the modulos(len) of an array.
    @param: array => list or numpy array.
    """
    return math.sqrt(sum(array ** 2))

def vectorNorm(array):
    return array / vectorMod(array)

def csvImport(file_name):
	fhand = open(file_name, 'r')
	raw_data = [",".join(line.split(',')[:2]) for line in fhand]
	raw_data = [float(element) for element in ",".join(raw_data).split(",")]
	data = np.array(raw_data).reshape(math.ceil(len(raw_data) / 2), 2)

	return data


data = csvImport("iris-data.csv")
# data = np.array([vectorNorm(line) for line in data])

fig = plt.figure(1)
plt.subplot(211)
plt.scatter(data[:, 0], data[:, 1], s=50)

solver = KMeans(data, 4)
cluster_data = solver.clustering()
print (cluster_data)
centorids = solver.getCentroids()

plt.subplot(212)
plt.scatter(data[:, 0], data[:, 1], c=cluster_data, s=50, cmap='rainbow')
plt.scatter(centorids[:, 0], centorids[:, 1], marker='*', s=50)

plt.show() 