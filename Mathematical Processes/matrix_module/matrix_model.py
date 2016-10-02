import numpy as np

def euclidianDist(point_one, point_two):
        """
        @Info: Calculate the euclidian distance between two points.
        @param: point_one :: np.array
        @param: point_two :: np.array
        @return: float
        """
        return np.sqrt(sum((point_one - point_two) ** 2))