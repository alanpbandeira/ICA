import numpy as np


def gaussian_func(x, a, b, c):
    e_pow = -(np.power((x - b), 2) / 2 * np.power(c, 2))

    return a * np.exp(e_pow)

