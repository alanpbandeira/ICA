import numpy as np

def euclidianDist(point_one, point_two):
        """
        @Info: Calculate the euclidian distance between two points.
        @param: point_one :: np.array
        @param: point_two :: np.array
        @return: float
        """
        return np.sqrt(sum((point_one - point_two) ** 2))

def vectorMod(array):
    """
    @Info: Returns the modulos(len) of an array.
    @param: array => list or numpy array.
    """
    return math.sqrt(sum(array ** 2))

def vectorNorm(array):
    return array / vectorMod(array)