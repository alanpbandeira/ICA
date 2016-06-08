import numpy as np


class MutationOperator:
    def __init__(self, mutation_prob, n_target_genes):
        self.mutation_prob  = mutation_prob
        self.n_target_genes = n_target_genes

    def bitFlipMutation(self, array):
        n = 0
        genes = np.random.randint(0, len(array), self.n_target_genes)

        for gene in genes:
            tester = np.random.random_sample()

            if tester < self.mutation_prob:
                if array[gene] == 1:
                    array[n] = 0
                else:
                    array[gene] = 1