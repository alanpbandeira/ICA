import numpy as np


def bitFlipMutation(individual_list, mutation_prob=0.05, n_target_genes=3):
    """
    Applies a bit_flip mutation to an individual
    :param individual_list:
    :param mutation_prob: default probability of flipping a bit
    :param n_target_genes:
    :return:
    """

    genes = np.random.randint(0, len(individual_list), n_target_genes)

    for gene in genes:
        tester = np.random.random_sample()

        if tester < mutation_prob:
            if individual_list[gene] == 1:
                individual_list[gene] = 0
            else:
                individual_list[gene] = 1