import numpy as np
import math
from Visualization import visual_model as vm
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

solver = KMeans(data, 4)
cluster_data = solver.clustering()
centroids = solver.getCentroids()

vm.comparative_plot(data, cluster_data, centroids)