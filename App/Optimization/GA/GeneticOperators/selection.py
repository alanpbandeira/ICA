import numpy as np


def binaryTournament(population, identical_parent=False):
    """
    - Select an individual using the binaryTournament method.
    :param population:
    :param identical_parent:
    :return:
    """
    index_one = index_two = None
    if identical_parent:
        index_one = index_two = np.random.choice(x for x in range(population.individual_list))
    else:
        while index_one is not index_two:
            index_one = np.random.choice(x for x in range(population.individual_list))
            index_two = np.random.choice(x for x in range(population.individual_list))

    candidate_one = population.individual_list[index_one]
    candidate_two = population.individual_list[index_two]

    if candidate_one.fitness >= candidate_two.fitness:
        return index_one
    else:
        return index_two


def rouletteWheel(population):
    fitness_total = 0

    for individual in population.individual_list:
        fitness_total += individual.fitness

    wheel = []
    section_base = 0

    for individual in population.individual_list:
        section_upper_range = section_base + individual.fitness / fitness_total
        wheel.append((section_upper_range, individual.id))
        section_base = section_upper_range

    selector = np.random.random_sample()

    for section in wheel:
        if selector < section[0]:
            return wheel.index(section)




