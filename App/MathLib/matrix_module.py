import numpy as np

def euclidian_dist(point_one, point_two):
    """
    Calculate the euclidian distance between two points.
    
    :param point_one: np.array
    :param point_two: np.array
    :return float: 
    """
    return np.sqrt(sum((point_one - point_two) ** 2))

def vector_mod(array):
    """
    Returns the modulos(len) of an array.
    
    :param array: List or scalar.
    """
    
    return np.sqrt(sum(array ** 2))

def vector_norm(array):
    """
    :param array: numpy array
    """
    
    return array / vector_mod(array)

def linear_combination(scalar_vector, vector_list):
    """
    :param scalar_vector: Scalar values for linear combination.
    :param vector_lsit: Vectors to the combination. Must match scalar order.
    """
    
    return np.transpose(np.matrix(scalar_vector) * np.matrix(vector_list))