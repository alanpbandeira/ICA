import numpy as np
import math


def expected_value(setVariables, probVariables=None):
	"""
	Return the expected value of a given set variables and its probability.

	:param setVariables: An array of variables.
	
	:param estimated: The default value shuold be use to express that all 
	variables presents the same probability, otherwise a set of probabilities 
	matching the set of variables must be provided.
	"""
	
	if probVariables is not None:
		values = [x * p for x, p in zip(setVariables, probVariables)]
		return sum(values) / len(values)
	else:
		return sum(setVariables) / len(setVariables)
	
def variance(setVariables, probVariables=None):
	"""
	Return the variance of a given set variables and its probability.

	:param setVariables: An array of variables.
	
	:param estimated: The default value shuold be use to express that all 
	variables presents the same probability, otherwise a set of probabilities 
	matching the set of variables must be provided.
	"""

	mean = expected_value(setVariables, probVariables)
	return sum([(x - mean) ** 2 for x in setVariables]) / len(setVariables)

def standart_deviation(setVariables, probVariables=None):
	"""
	Return the standart deviation of a given set variables and its probability.

	:param setVariables: An array of variables.
	
	:param estimated: The default value shuold be use to express that all 
	variables presents the same probability, otherwise a set of probabilities 
	matching the set of variables must be provided.
	"""

	return math.sqrt(variance(setVariables, probVariables))

