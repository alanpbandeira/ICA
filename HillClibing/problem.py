import math

class Problem():
	"""docstring for Problem"""

	def __init__(self, maximization, interval):
		self.maximization = maximization
		self.interval = interval

	@staticmethod
	def objective_function_one(x):
		element_one = -2 * math.pow(((x - 0.1) / 0.9), 2)
		element_two = math.pow(math.sin(5 * math.pi * x), 6)
		result = math.pow(2, element_one) * element_two
		return result

	@staticmethod
	def objective_function_two(x, y):
		element_one = math.exp(-(math.pow(x, 2) + math.pow(y, 2)))
		


	def setScore(self, value):
		return self.objective_function(value)