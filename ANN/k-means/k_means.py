import numpy as np

class KMeans(object):
    
    def __init__(self, data, n_clusters):
        self.data = data
        self.n_clusters = n_clusters
    
    def selectRandomCentroids(self):
        centroids = np.random.choice(len(self.data), self.n_clusters)
        init_centoids = np.array([self.data[centroid] for centroid in centroids])

    def setCentroids():
        pass
    
    def setClusters(self):
        pass
    
    @staticmethod
    def distanceCalc():
        pass
    
    def clustering(self):
        centroids = self.selectRandomCentroids()

        while True:
            distanceCalc()
            setClusters()
            setCentroids()
