import math, random
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def objectiveFunctionOne(value):

	result = math.pow(value, 2) - (4 * value) + 3
	
	return result

def objectiveFunctionTow(value):
	
	result = math.exp(-value) + math.pow(value, 2)

	return result

def evaluationFunction(candidate_value, current_value, objective_function):
	candidate_score = objective_function(candidate_value)
	current_score   = objective_function(current_value)

	if (candidate_score < current_score):
		return candidate_value
	else:
		return current_value

def pertubator(value):
	new_value = value - 0.01
	return new_value

# Plots the grahp of the events os the optimization
# over the graph of the objective function in accor-
# with the parameters.
#
# @param: function - Objective function.
# @param: x_axis   - Array of values over the x axis.
# @param: range_x  - Tuple of starting and ending plot 
# 					 points fot the x axis
# @param: delta    - The value for the icrementaion step
#					 of the function plot.
#
def comparativePlot(function, x_axis, data_out):
	generic_array_x = list()
	generic_array_y = list()

	y_axis = list()
	
	for x in range(-100, 100):
		generic_array_x.append(x)
		generic_array_y.append(function(x))

	#for x in frange(range_x[0], range_x[1], delta):
	#	generic_array_x.append(x)
	#	generic_array_y.append(function(x))

	for x in x_axis:
		y_axis.append(function(x))

	range_y = ( y_axis[0], y_axis[len(y_axis) - 1] )

	plt.plot(generic_array_x, generic_array_y, 'b', x_axis, y_axis, 'ro')
	plt.axis([-10, 10, -10, 100])
	#plt.show()
	plt.savefig((data_out + '.png'))


def hillClibing(goal,
				max_iterations, 
				objective_function, 
				evaluation_function, 
				petubation_function,
				data_out):
	
	fhand = open((data_out + '.txt'), 'a')
	value_list = list()
	candidate_value = random.uniform(0, 3)
	candidate_score = objective_function(candidate_value)
		
	best_result = candidate_value
	best_score  = candidate_score
	improvement = True
	iterations  = 1
	value_list.append(best_result)

	fhand.write('Best value\t\t\t\t\tBest Score\t\t\t\t\tIterations\n')
	fhand.write(str(best_result) + "\t\t\t" + str(best_score) + "\t\t\t\t" + str(iterations) + "\n")
	
	while ((iterations <= max_iterations) and (best_result != goal) and improvement):
		candidate_value = pertubator(candidate_value)
		candidate_score = objective_function(candidate_value)

		best_result = evaluationFunction(candidate_value, best_result, objective_function)

		if best_result != candidate_value:
			improvement = False

		value_list.append(best_result)
		iterations += 1
		fhand.write(str(best_result) + "\t\t\t" + str(best_score) + "\t\t\t\t" + str(iterations) + "\n")

	fhand.write('\n')

	comparativePlot(objective_function, value_list, data_out)

#for x in range(100):
#hillClibing(0.1, 1000, objectiveFunctionOne, evaluationFunction, pertubator, 'Data_output - 1a')
#hillClibing(0.01, 1000, objectiveFunctionOne, evaluationFunction, pertubator, 'Data_output - 1b')
#hillClibing(0.01, 1000, objectiveFunctionTow, evaluationFunction, pertubator, 'Data_output - 2a')
hillClibing(0.001, 1000, objectiveFunctionTow, evaluationFunction, pertubator, 'Data_output - 2b')


