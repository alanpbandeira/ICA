"""
This is an old code kept here to be revised whenever.

"""


import numpy as np

from .neuron_model import Neuron
from ...ANN.MathLib.matrix_module import euclidianDist


class NeuronLayer(object):
	"""
	docstring for NeuronSet
	"""

#
#	DUNDER METHODS
#

	def __init__(self, data_set, dimensions, n_radius):
		"""
		@param: dimensions: Dimensions of the NeuronLayer matrix (rows, columns);
		@param: n_radius: Neighbourhood radius.
		"""

		self._radius = n_radius
		self._dimensions = dimensions
		self._size = _dimensions[0] * _dimensions[1]

		self._indexes = self.genLayerIndexes() 
		self._neurons = self.neuronsFromData(data_set)
		self._layer_map = self.buildLayer()

	def __len__(self):
		return len(self._layer_map)

	def __getitem__(self, index):
		return self._layer_map[index]

	def __setitem__(self, key, value):
		self._layer_map[key] = value

#
#	CLASS METHODS
#

	def neuronsFromData(self, data_set):
		"""
		Select data points to compound the neuronset

		@param: data_set: DataSet Object or array of data Objects.
		"""

		if len(data_set) == self.size:
			candidates = data_set
		elif len(data_set) < self.size:
			return "Insuficient Data"
		else:
			candidate = []
			count = 0
			while count < self.size:
				candidate = np.random.choice(data_set)
				if candidate in candidates:
					continue
				else:
					candidates.append(candidate)
					count += 1

		return [Neuron(candidate.data) for candidate in candidates]

	def genLayerIndexes(self):
		"""
		Create matrix-like indexes to the layer with linear complexity.
		"""

		indexes = []

		if self._size < 1:
			raise ValueError("Impossible to create zero-sided layer")

		x_counter = 1
		y_counter = 1

		while x_counter <= self._dimensions[0]:
			if y_counter <= self._dimensions[1]:
				indexes.append([x_counter, y_counter])
				y_counter += 1
			else:
				x_counter += 1

		return indexes

	def setNeighbours(self):
		"""
		"""

		for neuron in self._neurons:
			candidates = []

			for candidate in self._neurons:
				if candidate is neuron:
					continue

				p_one = np.array(neuron.index)
				p_two = np.array(candidate.index)
				if euclidianDist(p_one, p_two) <= self._radius:
					candidates.append(candidate.index)

	def buildLayer(self, data_set):
		"""
		"""

		class_ids = range(1, (self._size + 1))

		for idx, c_id in zip(self._indexes, class_ids):
			elected_neu = np.random.choice(range(self._size))
			self._neurons[elected_neu].index(idx)
			self._neurons[elected_neu].class_id(c_id)


		# set neighbours !TO DO!





#
#	PROPERTIES
#
