import math
import matplotlib.pyplot as plt
from problem import Problem

plt.style.use('ggplot')

class Plotter():
	"""docstring for Plotter"""
	def __init__(self, problem):
		self.problem = problem
	
	def samplePlot(self, y_interval):
		x_axis = list()
		y_axis = list()
		x_range = self.problem.interval

		while x_range[0] <= x_range[1]:
			x_axis.append(x_range[0])
			y_axis.append(self.problem.objective_function(x_range[0]))
			x_range = (x_range[0] + 0.01, x_range[1])

		plt.plot(x_axis, y_axis, 'b')
		plt.axis([self.problem.interval[0], 
				  self.problem.interval[1], 
				  y_interval[0], y_interval[1]])

	def pointPlot(self, x_value, y_value, y_interval):
		plt.plot(x_value, y_value, 'ro')
		plt.axis([self.problem.interval[0], self.problem.interval[1], y_interval[0], y_interval[1]])
