import random
import numpy as np


class Individual:

    """

    """

    chromosome = np.array([])

    def __init__(self, n_genes=4, rand=False, score=None):
        self.n_genes = n_genes
        self.score   = score

        if rand:
            self.setRandomIndividual()

    def setRandomIndividual(self):
        coin = random.randint(1, 10)

        if coin <= 5:
            np.append(self.chromosome, 1)
        else:
            np.append(self.chromosome, 0)

