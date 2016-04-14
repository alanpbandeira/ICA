from problem import Problem
import random

class HillClibing:
	"""docstring for HillClibing"""
	
	def __init__(self, max_iterations, problem):
		self.max_iterations = max_iterations
		self.problem = problem

	# Nota: limitar o pertubador para o limitante
	
	def randomPertubator(self,value, maximize):
		if maximize is True:
			#pertubation = self.problem.interval[]
			return value + random.random()
		else:
			return value - random.random()

	def run(self):
		maximization    = self.problem.maximization
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
		