import numpy as np
from ..Population.population import Population
from ..problem import Problem
from ..GeneticOperators import crossover, mutation, selection


class GA:
    result_list = []

    def __init__(self, problem, max_generations=100):
        self.max_generations = max_generations
        self.problem = problem

    def run(self):
        initial_population = Population()

        # Evaluates the initial population
        for individual in initial_population.individual_list:
            index = initial_population.individual_list.index(individual)
            initial_population.individual_list[index].fitness(self.problem.setScore(individual.n_value))

        best_individual = (initial_population.individual_list[0].fitness,
                           initial_population.individual_list[0].individual_id)

        for individual in initial_population.individual_list:
            if individual.fitness > best_individual[0]:
                best_individual = individual.fitness, individual.individual_id

        self.result_list.append(best_individual)

        # Select next population parents
        elected_parents = np.array([])
        while len(elected_parents) < (initial_population.individual_list / 2):
            elected = selection.rouletteWheel(initial_population)
            if elected not in elected_parents:
                elected_parents = np.append(elected_parents, initial_population.individual_list[elected])
            else:
                continue

        generations = 1

        while generations <= self.max_generations:
            # Initiate a new generation
            new_generation = []

            # Apply reproductions to the parents without using two equals elements fo parents
            while len(new_generation) < initial_population.size:
                parent_one = np.random.choice(elected_parents)
                parent_two = np.random.choice(elected_parents)

                if parent_one is not parent_two:
                    offspring = crossover.singlePoint([parent_one.chromosome, parent_two.chromosome])
                    new_generation.append(offspring[0])
                    new_generation.append(offspring[1])
                else:
                    continue

            # Apply mutation to the new generation
            mutation.bitFlipMutation(new_generation)

            # Instantiate the new Population from the new generated individuals
            new_population = Population(new_generation)

            # Evaluates each new individual
            for individual in new_population.individual_list:
                index = new_population.individual_list.index(individual)
                new_population.individual_list[index].fitness(self.problem.setScore(individual.n_value))

            # Select the next generation parents
            elected_parents = np.array([])
            while len(elected_parents) < (new_population.individual_list / 2):
                elected = selection.rouletteWheel(new_population)
                if elected not in elected_parents:
                    elected_parents = np.append(elected_parents, initial_population.individual_list[elected])
                else:
                    continue

            generations += 1

            for individual in new_population.individual_list:
                if individual.fitness > best_individual[0]:
                    best_individual = individual.fitness, individual.individual_id

            self.result_list.append(best_individual)

        return self.result_list[len(self.result_list) - 1]
