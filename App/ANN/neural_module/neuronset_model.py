import numpy as np

from .neuron_model import Neuron
from .set_builder import LayerBuilder
from ...MathLib.matrix_module import euclidianDist


class NeuronLayer(object):
	"""
	docstring for NeuronSet
	"""

#
#	DUNDER METHODS
#

	def __init__(self, neuron_size, dimensions, n_radius):
		"""
		@param: dimensions: Dimensions of the NeuronLayer 
		indexes (rows, columns);
		@param: n_radius: Neighbourhood radius for each neuron.
		"""

		self._radius = n_radius
		self._dimensions = dimensions
		self._size = self._dimensions[0] * self._dimensions[1]

		lb = LayerBuilder(self._size, self._dimensions, self._radius)
		
		self._layer_map = lb.build(neuron_size)

	def __len__(self):
		return len(self._layer_map)

	def __getitem__(self, index):
		return self._layer_map[index]

	def __setitem__(self, key, value):
		self._layer_map[key] = value

#
#	CLASS METHODS
#

	def weightMatrix(self):
		"""
		Return matrix representing the layer by neuron wheights 

		"""
		new_matrix = np.zeros(self._dimensions)

		for item in self._layer_map.items():
			new_matrix[item[0][0]][item[0][1]] = item[1].wheights

		return new_matrix

#
#	PROPERTIES
#
	
	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, value):
		self._radius = value

	@property
	def dimensions(self):
		return self._dimensions

	@dimensions.setter
	def dimensions(self, tuple):
		self._dimensions = value

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		self._size = value
