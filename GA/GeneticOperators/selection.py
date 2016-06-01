from ..IndividualModel.individual import Individual
from ..Population.population import Population
import numpy as np


class Selection:
    def __init__(self, population):
        self.population = population

    def rouletteWheel(self):
        population_fitness = 0
        for individual in self.population.individual_list:
            population_fitness += individual.fitness

        section_base = 0
        wheel = []

        for individual in self.population.individual_list:
            section_upper_range = section_base + individual.fitness / population_fitness
            wheel.append((section_upper_range, individual.id))
            section_base =

        selector = np.random.random_sample()

        for section in wheel: if




