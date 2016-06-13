import numpy as np


def singlePoint(parent_list):
    point = np.random.randint(0, (len(parent_list[0])), 1)[0]
    child_one = np.concatenate((parent_list[0][0:point], parent_list[1][point:]))
    child_two = np.concatenate((parent_list[1][0:point], parent_list[0][point:]))

    return child_one, child_two


def twoPoint():
    """
    TODO!!!
    :return: NOTHING YET!
    """
    pass
