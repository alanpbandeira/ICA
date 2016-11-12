import numpy as np
from .matrix_module import euclidian_dist


def scalar_gaussian_func(x, a, b, c):
	"""
	"""
    e_pow = -(np.power((x - b), 2) / 2 * np.power(c, 2))

    return a * np.exp(e_pow)

def vect_gaussian_func(pOne, a, pTwo, c):
	"""
	"""
    e_pow = -(np.power(euclidian_dist(pOne - pTwo), 2) / 2 * np.power(c, 2))

    return a * np.exp(e_pow)