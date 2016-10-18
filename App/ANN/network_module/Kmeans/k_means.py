import numpy as np
import math

class KMeans(object):
    
    def __init__(self, data, n_clusters):
        """
        @param: data :: numpy array
        @param: n_clusters :: int
        @attribute: clusters :: map
        @attribute: centroids :: map
        """
        self.data = data
        self.n_clusters = n_clusters
        self.clusters = None
        self.centroids = None
    
    @staticmethod
    def euclidianDist(point_one, point_two):
        """
        @Info: Calculate the euclidian distance between two points.
        @param: point_one :: np.array
        @param: point_two :: np.array
        @return: float
        """
        d_sum = 0
        for p, q in zip(point_one, point_two):
            d_sum += (p - q) ** 2

        return math.sqrt(d_sum)

    def getCentroids(self):
        """
        @Info: Returns a numpy array of the cntroid points in order of cluster.
        @return: n-dimensional numpy array
        """
        return np.array([point for cluster, point in self.centroids.items()]).reshape(self.n_clusters, 2)

    def setClusterList(self):
        """
        @info: Return a list of clusters matching the data sorting.
        @return: data_list :: list object
        """
        data_list = []
        for point in self.data:
            distances = []
            for cluster, centroid in self.centroids.items():
                distances.append((self.euclidianDist(point, centroid), cluster))
            data_list.append(min(distances)[1])

        return data_list

    def selectRandomCentroids(self):
        """
        @Info: Randomly selects n poits for centroids.
        @return: dict :: {cluster: point}
        """
        centroids = np.random.choice(len(self.data), self.n_clusters)
        return {c: p for p, c in zip([self.data[centroid,:] for centroid in centroids], range(1, self.n_clusters + 1))}

    def setClusters(self):
        """
        @Info: Assigns a list of points to its` respective 
               clusters as a dict structure :: {cluster: [points]}
        """
        if self.clusters is None:
            curr_centroids = [self.centroids[x] for x in self.centroids]
            self.clusters = {c: [p] for c, p in zip(range(1, self.n_clusters + 1), curr_centroids)}
        else:
            self.clusters = {c: None for c in self.centroids}

        for point in self.data:
            distances = []
            
            for cluster, centroid in self.centroids.items():
                distances.append((self.euclidianDist(point, centroid), cluster))
            
            elected = min(distances)
            
            if self.clusters[elected[1]] is None:
                self.clusters[elected[1]] = [point]
            else:   
                self.clusters[elected[1]].append(point)

    def calcCentroids(self):
        """
        @Info: Calculate a new centroid based on the data points of each cluster.
        """
        for cluster, points in self.clusters.items():
            self.centroids[cluster] = sum(points) / len(points)
    
    def clustering(self):
        """
        @Info: Execute k-means the clustering process.
        @return: List of clusters sorted to match the data set order :: list object. 
        """
        self.centroids = self.selectRandomCentroids()
        epochs = 100
        
        # Uncoment the code bellow to get the initial centroids
        #
        # print(self.getCentroids())

        while epochs > 0:
            epochs -= 1
            
            self.setClusters()
            self.calcCentroids()

        # Uncoment the code bellow to get the final centroids
        #
        # print(self.getCentroids())

        return self.setClusterList()