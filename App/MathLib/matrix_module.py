import numpy as np

def euclidian_dist(point_one, point_two):
        """
        @Info: Calculate the euclidian distance between two points.
        @param: point_one :: np.array
        @param: point_two :: np.array
        @return: float
        """
        return np.sqrt(sum((point_one - point_two) ** 2))

def vector_mod(array):
    """
    @Info: Returns the modulos(len) of an array.
    @param: array => list or numpy array.
    """
    return np.sqrt(sum(array ** 2))

def vector_norm(array):
    return array / vectorMod(array)

def linear_combination(scalar_vector, vector_list):
    """
    @param: scalar_vector: Scalar values for linear combination.
    @param: vector_lsit: Vectors to the combination. Must match scalar order.
    """
    return np.transpose(np.matrix(scalar_vector) * np.matrix(vector_list))