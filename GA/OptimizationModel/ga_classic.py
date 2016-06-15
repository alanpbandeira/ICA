import numpy as np
from ICA.GA.Population.population import Population
from ICA.GA.problem import Problem
from ICA.GA.GeneticOperators import crossover, mutation, selection


class GA:

    result_list = []

    def __init__(self, problem, max_generations=100):
        self.max_generations = max_generations
        self.problem = problem

    def run(self, n_elected_parents):
        initial_population = Population()

        for individual in initial_population.individual_list:
            index = initial_population.individual_list.index(individual)
            initial_population.individual_list[index].fitness(self.problem.setScore(individual.n_value()))

        elected_parents = [selection.rouletteWheel(initial_population)
                           for x in range(1, (initial_population.size / 2)), 1]




