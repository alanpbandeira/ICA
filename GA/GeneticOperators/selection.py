import numpy as np


def binaryTournament(population, identical_parent=False):
    index_one = index_two = None
    if identical_parent:
        while index_one == index_two:
            index_one = np.random.randint(0, len(population.individual_list), 1)[0]
            index_two = np.random.randint(0, len(population.individual_list), 1)[0]
    else:
        index_one = np.random.randint(0, len(population.individual_list), 1)[0]
        index_two = np.random.randint(0, len(population.individual_list), 1)[0]

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




