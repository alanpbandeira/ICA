import numpy as np


def bitFlipMutation(individual, mutation_prob=0.05, n_target_genes=3):
    """
    Applies a bitflip mutation to an individual
    :param individual:
    :param mutation_prob:
    :param n_target_genes:
    :return:
    """
    n = 0
    genes = np.random.randint(0, len(individual), n_target_genes)

    for gene in genes:
        tester = np.random.random_sample()

        if tester < mutation_prob:
            if individual[gene] == 1:
                individual[n] = 0
            else:
                individual[gene] = 1