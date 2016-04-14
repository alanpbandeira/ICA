import math

class Problem():
	"""docstring for Problem"""

	def __init__(self, maximization, interval):
		self.maximization = maximization
		self.interval = interval

	@staticmethod
	def objective_function(x):
		element_one = -2 * math.pow(((x - 0.1) / 0.9), 2)
		element_two = math.pow(math.sin(5 * math.pi * x), 6)
		result = math.pow(2, element_one) * element_two
		return result

	def setScore(self, value):
		return self.objective_function(value)

	def evaluate(self, current_value, candidate_value):
		candidate_score = self.setScore(candidate_value)
		current_score   = self.setScore(current_value)

		if self.maximization:
			if (candidate_score > current_score):
				return candidate_value
			else:
				return current_value
		else:
			if (candidate_score < current_score):
				return candidate_value
			else:
				return current_value