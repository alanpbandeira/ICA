import numpy as np


class CrossoverOperator:
    def __init__(self, parent_list, offspring_size=2):
        self.parent_list = parent_list
        self.offspring_size = offspring_size

    def singlePoint(self):
        point = np.random.randint(0, (len(self.parent_list[0])), 1)[0]
        child_one = np.concatenate((self.parent_list[0][0:point], self.parent_list[1][point:]))
        child_two = np.concatenate((self.parent_list[1][0:point], self.parent_list[0][point:]))

        return child_one, child_two

    def twoPoint(self):
        """
        TODO!!!
        :return: NOTHING YET!
        """
        pass
