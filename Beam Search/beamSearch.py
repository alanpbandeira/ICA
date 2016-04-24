from problem import Problem
import math, random

class BeamSearch():
	"""docstring for BeamSearch"""

	result_list = list()
	population  = list()
	
	def __init__(self, task_problem, population_size, population_beam):
		self.problem  = task_problem
		self.population_size = population_size
		self.beam_size = math.floor(population_beam * self.population_size)
		self.interval = self.problem.interval

	def initRandomPopulation(self):
		for item in range(self.population_size):
			individual = random.uniform(self.interval[0], self.interval[1])
			invidual_score = self.problem.setScore(individual)
			self.population.append((invidual_score, individual))

	def randomPertubator(self, value):		
		increase = None

		if random.uniform(0, 1) > 0.5:
			increase = True

		if increase:
			pertubation = random.uniform(0, 0.1)
			new_value   = value + pertubation
		else:
			pertubation = random.uniform(0, 0.1)
			new_value   = value - pertubation

		return new_value

	def run(self, max_iterations):
		self.initRandomPopulation()
		beam = []

		iterations = 0		

		while iterations < max_iterations:
			self.population.sort(reverse = True)
			beam = self.population[:self.beam_size]
			best_result = beam[0]
			
			next_generation = []

			for individual in range(len(self.population)):
				selection = random.randint(0, (self.beam_size - 1))
				father_infividual = beam[selection]
				new_individual = self.randomPertubator(father_infividual[1])
				new_individual_score = self.problem.setScore(new_individual)
				next_generation.append((new_individual_score, new_individual))

			self.population = next_generation
			iterations += 1

		self.result_list.append((best_result[1], best_result[0]))

		return (iterations, best_result[1], best_result[0])




			

		


