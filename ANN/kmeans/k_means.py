import numpy as np
import math

class KMeans(object):
    
    def __init__(self, data, n_clusters):
        """
        @param data => numpy array
        @param n_clusters => int
        @param clusters => map
        @param centroids => map
        """
        self.data = data
        self.n_clusters = n_clusters
        self.clusters = None
        self.centroids = None
    
    @staticmethod
    def euclidianDist(point_one, point_two):
        d_sum = 0
        for p, q in zip(point_one, point_two):
            d_sum += (p - q) ** 2

        return math.sqrt(d_sum)

    def selectRandomCentroids(self):
        centroids = np.random.choice(len(self.data), self.n_clusters)
        # return np.array([self.data[centroid] for centroid in centroids])
        return {c:p for p, c in zip([self.data[centroid,:] for centroid in centroids], range(1, self.n_clusters + 1))}

    def setClusters(self):
        if self.clusters is None:
            self.clusters = {c:[p] for c, p in zip(range(1, self.n_clusters + 1), [self.centroids[x] for x in self.centroids])}
        else:
            self.clusters = {c:None for c in self.centroids}

        for point in self.data:
            distances = []
            
            for cluster, centroid in self.centroids.items():
                distances.append((self.euclidianDist(point, centroid), cluster))
            
            elected = min(distances)
            
            if self.clusters[elected[1]] is None:
                self.clusters[elected[1]] = [point]
            else:
                # print(self.clusters[elected[1]])    
                self.clusters[elected[1]].append(point)

    def setCentroids(self):
        for cluster, points in self.clusters.items():
            #print(cluster, points)
            self.centroids[cluster] = sum(points) / len(points)
    
    def clustering(self):
        cluter_data = []
        self.centroids = self.selectRandomCentroids()
        # converged = False
        count = 10

        while not converged:
            count -= 1
            
            # actual_centroids = self.centroids.copy()
            self.setClusters()
            self.setCentroids()

            # if actual_centroids is self.centroids:
            #     #count += 1
            #     converged = True
            # if count > 10:
            #     converged = True

        #print(self.clusters)

        for cluster, points in self.clusters.items():
            for point in self.data:
                if point in points:
                    cluster_data.append(cluster)

        return cluster_data
