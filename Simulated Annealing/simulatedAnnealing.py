from problem import Problem
import random, math

class SimulatedAnnealing():
	"""docstring for SimulatedAnnealing"""

	result_list = list()

	def __init__(self, task_problem, final_temperature):
		self.problem = task_problem
		self.final_temperature = final_temperature

	def setInitTemperature(self, trial_max_iterations):
		deltaScore_temperature_list = list()
		interval    = self.problem.interval

		best_value  = random.uniform(interval[0], interval[1])
		best_score  = self.problem.setScore(best_value)
		iterations  = 1
		attempts    = 1

		while iterations < trial_max_iterations:
			candidate_value = self.randomPertubator(best_value)
			candidate_score = self.problem.setScore(candidate_value)

			if candidate_score > best_score:
				deltaScore_temperature_list.append(candidate_score - best_score)
				best_value = candidate_value
			else:
				attempts += 1
				continue

			attempts += 1
			iterations += 1

		avarage_improve = sum(deltaScore_temperature_list) / len(deltaScore_temperature_list)
		init_acept_prob = iterations / attempts

		return avarage_improve / math.log(init_acept_prob)

	def coolingFunction(self, temperature, init_temperature, max_epoch):
		alpha_expoent = 1 / (max_epoch - 1)
		alpha = math.pow((self.final_temperature / init_temperature), alpha_expoent)

		new_temperature =  alpha * temperature

		return new_temperature

	def randomPertubator(self, value):		
		increase = None

		if random.uniform(0,1) > 0.5:
			increase = True
		else:
			increase = False

		# This pertubation function allows the function 
		# leap to another optimun in the search space. 
		# Uncoment to use.
		#
		pertubation_range = self.problem.interval[1] - self.problem.interval[0]
		incrementation_range = pertubation_range - (value - self.problem.interval[0])
		decrementation_range = pertubation_range - incrementation_range

		if increase:
			pertubation = random.uniform(0, 0.01)
			new_value   = value + pertubation
		else:
			pertubation = random.uniform(0, 0.01)
			new_value   = value - pertubation

		return new_value

	def run(self, max_iterations):
		initial_temperature = self.setInitTemperature(100)
		print (initial_temperature)
		
		temperature = initial_temperature
		interval    = self.problem.interval

		best_value  = random.uniform(interval[0], interval[1])
		best_score  = self.problem.setScore(best_value)
		iterations  = 1

		while iterations < max_iterations:
			candidate_value = self.randomPertubator(best_value)
			candidate_score = self.problem.setScore(candidate_value)

			deltaScore_temperature_ratio = (candidate_score - best_score) / temperature

			if candidate_score > best_score:
				best_value = candidate_value
			elif (random.uniform(0,1) > math.exp(deltaScore_temperature_ratio)):
				best_score = candidate_score

			temperature = self.coolingFunction(temperature, initial_temperature, max_iterations)
			iterations += 1

		self.result_list.append((best_value, best_score))
		return ((iterations, best_value, best_score))
			