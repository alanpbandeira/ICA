import numpy as np
import math

class KMeans(object):
    
    def __init__(self, data, n_clusters):
        self.data = data
        self.n_clusters = n_clusters
        self.clusters = {}
    
    @staticmethod
    def euclidianDist(point_one, point_two):
        d_sum = 0
        
        for p, q in zip(point_one, point_two):
            d_sum += (p - q) ** 2

        return math.sqrt(d_sum)

    def selectRandomCentroids(self):
        centroids = np.random.choice(len(self.data), self.n_clusters)
        return np.array([self.data[centroid] for centroid in centroids])

    def setClusters(self):
        clusters = []

        distanceCalc()
        pass

    def setCentroids():
        pass
    
    
    def clustering(self):
        init_clusters = selectRandomCentroids()

        self.clusters = {c:p for c, p in zip(range(1, n_clusters + 1), init_clusters)}

        init_clusters = self.selectRandomCentroids()

        while True:
            setClusters()
            setCentroids()
