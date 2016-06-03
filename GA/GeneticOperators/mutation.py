import numpy as np


class MutationOperator:
    def __init__(self, mutation_prob):
        self.mutation_prob = mutation_prob

    @staticmethod
    def hitTester(hit_probability, floor=0, limit=10000):

        test = np.random.randint(floor, limit, 1)[0]


    def bitFlipMutation(self, array):
        n = 0
        while n < len(array):
            tester = np.random.random_sample(1)[0]

            # TODO!
            if tester < 1:
                pass