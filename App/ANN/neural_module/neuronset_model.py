import numpy as np

from .neuron_model import Neuron


class NeuronLayer(object):
	"""
	docstring for NeuronSet
	"""
	
	def __init__(self, size, dimensions):
		"""
		@param: size: The number of neurons.
		@param: dimensions: Dimensions of the NeuronLayer matrix (rows, columns)
		"""
		self._size = size
		self._layer_dim = dimensions
		self._neuron_layer = None

	def __len__(self):
		return len(self._neuron_layer)

	def __getitem__(self, index_one, index_two=None):
		if index_two:
			return self._neuron_layer[index_one][index_two]
		else:
			return self._neuron_layer[index_one]

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

	def buildLayer(self):
		pass


