import numpy as np

from .neuron import Neuron
from .set_builder import LayerBuilder
from ...MathLib.matrix_module import vector_norm, euclidian_dist


class NeuronLayer(object):
	"""
	docstring for NeuronSet
	"""

#
#	DUNDER METHODS
#

	def __init__(self, neuron_size, dimensions, n_radius, data=None):
		"""
		@param: dimensions: Dimensions of the NeuronLayer 
		indexes (rows, columns);
		@param: n_radius: Neighbourhood radius for each neuron.
		"""

		self.network = "Kohonen Self-Organizing Maps"
		self._radius = n_radius
		self._dimensions = dimensions
		self._size = self._dimensions[0] * self._dimensions[1]

		lb = LayerBuilder(self._size, self._dimensions, self._radius)
		
		if data is not None:
			self._layer_map = lb.build(neuron_size, data_set=data)
		else:
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

	def network_model(self):
		"""

		"""
		
		return self.network

	def weight_matrix(self):
		"""
		Return matrix representing the layer by neuron wheights 

		"""
		
		values = []

		keys = sorted([element for element in self._layer_map.keys()])
		
		for line in range(1, (self._dimensions[0] + 1)): 
			lines = []
			for column in range(1, (self._dimensions[1] + 1)):
				if (line, column) in keys:
					lines.append(self._layer_map[(line, column)])
			values.append(lines)

		return np.array(values)

	def normalize(self):
		"""

		"""
		for neuron in self._layer_map:
			normalized = vector_norm(self._layer_map[neuron].weights)
			self._layer_map[neuron].weights = normalized

	def update_neighbourhood(self):
		"""
		
		"""

		for idx in self._layer_map:
			candidates = []
			for candidate in self._layer_map:
				if  candidate == idx:
					continue
				else:
					p_one = np.array(idx)
					p_two = np.array(candidate)
					if euclidian_dist(p_one, p_two) <= self._radius:
						candidates.append(candidate)
			self._layer_map[idx].neighbourhood = candidates.copy()



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
