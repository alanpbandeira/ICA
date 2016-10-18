import numpy as np


def singlePoint(parent_list):
    point = np.random.randint(len(parent_list[0]))
    child_one = parent_list[0][0:point] + parent_list[1][point:]
    child_two = parent_list[1][0:point] + parent_list[0][point:]

    return child_one, child_two


def twoPoint():
    """
    TODO!!!
    :return: NOTHING YET!
    """
    pass
