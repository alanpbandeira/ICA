from ..IndividualModel.individual import Individual
from ..Population.population import Population


class Selection:
    def __init__(self, population):
        self.population = population

    def rouletteWheel(self):
        population_fitness = 0
        for individual in self.population.individual_list:
            population_fitness += individual.fitness

        section_base = 0
        wheel = {}

        for individual in self.population.individual_list:
            key = self.population.individual_list.index(individual)
            wheel[key] = section_base + individual.fitness / population_fitness
            section_base = wheel[key]

        


