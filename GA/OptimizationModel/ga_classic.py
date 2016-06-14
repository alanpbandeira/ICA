import numpy as np
from ..Population.population import Population
from ..problem import Problem
from ..GeneticOperators import crossover, mutation, selection


class GA:

    result_list = []

    def __init__(self, problem):
        self.problem = problem

    def run(self):
        initial_population = Population()

        for individual in initial_population.individual_list:
            index = initial_population.individual_list.index(individual)
            initial_population.individual_list[index].fitness(self.problem.setScore(individual.fitness()))

