import numpy as np

from ...MathLib.matrix_module import *


class Neuron(object):
	"""
	docstring for Neuron
	"""

	def __init__(self, weights=None, n_weights=None, value_range=None):
		"""
		Class that defines the Neuron object. If weights is given the others 

		@param: weights: 1D numpy array of numeric values, if no data is passed 
		the neuron will be set with an array of random values
		@param: n_weights: Number of weight that will compound the neuron randomly generated
		@param: range: Tuple of tow values, aa lower bound and an upper bound.
		"""
		if weights:
			self._weights = weights
			self.n_weights = len(self._weights)
		else:
			self.n_weights = n_weights
			self._weights = np.random.uniform(value_range[0], value_range[1], n_weights)
		
		self._norm = vectorMod(self._weights)
		self._neighbourhood = None
		self._class_id = None
		self._position = None

	@property
	def weights(self):
	 	return self._weights

	@weights.setter
	def weights(self, weights):
		self._weights = weights

	@property
	def norm(self):
		return self._norm

	@norm.setter
	def norm(self, new_norm):
		self._norm = new_norm

	@property
	def neighbourhood(self):
		return self._neighbourhood

	@neighbourhood.setter
	def neighbourhood(self, new_neighbourhood):
		self._neighbourhood = new_neighbourhood

	@property
	def class_id(self):
		return self._class_id

	@class_id.setter
	def class_id(self, new_id):
		self._class_id = new_id

	@property
	def position(self):
		return self._position

	@position.setter
	def position(self, new_position):
		self._position = new_position

	def activationFunc():
		pass # to do
