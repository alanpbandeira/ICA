import numpy as np

from .neuron_model import Neuron
from .set_builder import LayerBuilder as lb
from ...MathLib.matrix_module import euclidianDist
from ...ANN.Data.dataset_model import DataSet


class NeuronLayer(object):
	"""
	docstring for NeuronSet
	"""

#
#	DUNDER METHODS
#

	def __init__(self, neuron_size, dimensions, n_radius):
		"""
		@param: dataset: DataSet object used to 
		@param: dimensions: Dimensions of the NeuronLayer matrix (rows, columns);
		@param: n_radius: Neighbourhood radius.
		"""

		self._radius = n_radius
		self._dimensions = dimensions
		self._size = _dimensions[0] * _dimensions[1]
		self._layer_map = lb.build(self._size, self._dimensions, self._radius)

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
		new_matrix = np.zeros(self._dimensions)

		for item in 

#
#	PROPERTIES
#
