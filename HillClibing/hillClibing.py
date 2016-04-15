from problem import Problem
import random

class HillClibing:
	"""docstring for HillClibing"""
	
	def __init__(self, max_iterations, problem):
		self.max_iterations = max_iterations
		self.problem = problem

	def randomPertubator(self, value, maximize):
		min_interval = self.problem.interval[0]
		max_interval = self.problem.interval[1]
		
		if maximize is True:
			pertubation = random.uniform(0, (max_interval - value))
			return value + pertubation
		else:
			pertubation = random.uniform(0, (value - min_interval))
			return value - pertubation

	def run(self):
		maximization = self.problem.maximization
		candidate_value = random.uniform(self.problem.interval[0], self.problem.interval[1])
		candidate_score = self.problem.setScore(candidate_value)
			
		best_result = candidate_value
		best_score  = candidate_score
		improvement = True
		iterations  = 1
		
		while((iterations <= self.max_iterations) and improvement):

			candidate_value = self.randomPertubator(candidate_value, maximization)
			candidate_score = self.problem.setScore(candidate_value)

			best_result = self.problem.evaluate(candidate_value, best_result)

			if best_result != candidate_value:
				improvement = False

			iterations += 1

		return (iterations, best_result, self.problem.setScore(best_result))
		