import numpy as np

from ...MathLib.matrix_module import *


class Neuron(object):
	"""
	docstring for Neuron
	"""

	self._neighbourhood = None
	self._class_id = None
	self._index = None

#
#	DUNDER METHODS
#

	def __init__(self, weight_list=None, size=None):
		"""
		Class that defines the Neuron object. If weights is given the others 

		@param: weight_list: 1D numpy array of numeric values, if no data is passed 
		the neuron will be set with an array of random values
		@param: size: Number of weight that will compound the neuron randomly generated
		@param: range: Tuple of tow values, aa lower bound and an upper bound.
		"""
		if weight_list is not None:
			self._weights = weight_list
		else:
			self._weights = np.random.uniform(size)
		
		self._norm = vectorMod(self._weights)		

	def __len__(self):
		return len(self._weights)

	def __getitem__(self, index):
		return self._weights[index]

	def __setitem__(self, key, value):
		self._weights[key] = value


#
#	CLASS METHODS
#
	
	def activationFunc():
		pass # to do


#
#	PROPERTIES
#

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
	def index(self):
		return self._index

	@index.setter
	def index(self, new_index):
		self._index = new_index


