import numpy as np


class Selection:
    def __init__(self, population):
        self.population = population

    def rouletteWheel(self):
        population_fitness = 0
        for individual in self.population.individual_list:
            population_fitness += individual.fitness

        wheel = []
        section_base = 0

        for individual in self.population.individual_list:
            section_upper_range = section_base + individual.fitness / population_fitness
            wheel.append((section_upper_range, individual.id))
            section_base = section_upper_range

        selector = np.random.random_sample()

        for section in wheel:
            if selector < section[0]:
                return wheel.index(section)

    def binaryTournament(self, identical_parent=False):
        index_one = index_two = None
        if identical_parent:
            while index_one == index_two:
                index_one = np.random.randint(0, len(self.population.individual_list), 1)[0]
                index_two = np.random.randint(0, len(self.population.individual_list), 1)[0]
        else:
            index_one = np.random.randint(0, len(self.population.individual_list), 1)[0]
            index_two = np.random.randint(0, len(self.population.individual_list), 1)[0]

        candidate_one = self.population.individual_list[index_one]
        candidate_two = self.population.individual_list[index_two]

        if candidate_one.fitness >= candidate_two.fitness:
            return index_one
        else:
            return index_two




