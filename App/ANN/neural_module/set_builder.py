import numpy as np

from .neuron_model import Neuron


class LayerBuilder(object):
	"""docstring for Builder"""

	def __init__(self, layer_size, layer_dimensions, layer_radius):
		self.layer_radius = layer_radius
		self.layer_dimensions = layer_dimensions
		self.layer_size = layer_size
	
		
#
#	CLASS METHODS
#

	def neuronsFromData(self, data_set):
		"""
		Select data points to compound the neuronset

		@param: data_set: DataSet Object or array of data Objects.
		"""

		if len(data_set) == self.layer_size:
			candidates = data_set
		elif len(data_set) < self.layer_size:
			return "Insuficient Data"
		else:
			candidate = []
			count = 0
			while count < self.layer_size:
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

		if self.layer_size < 1:
			raise ValueError("Impossible to create zero-sided layer")

		x_counter = 1
		y_counter = 1

		while x_counter <= self.layer_dimensions[0]:
			if y_counter <= self.layer_dimensions[1]:
				indexes.append([x_counter, y_counter])
				y_counter += 1
			else:
				x_counter += 1

		return indexes

	def setNeighbours(self, neurons):
		"""

		"""

		for index in range(len(neurons)):
			candidates = []

			for candidate in neurons:
				if candidate is neurons[index]:
					continue
				else:
					p_one = np.array(neurons[index].index)
					p_two = np.array(candidate.index)
					if euclidianDist(p_one, p_two) <= self.layer_dimensions:
						candidates.append(candidate.index)

			neurons[index].neighbourhood = candidate.copy()


	def build(self, neuron_size):
		"""
		@param: neuron_size: TODO
		"""

		indexes = self.genLayerIndexes()
		neurons = [Neuron(neuron_size) for x in range(self.layer_size)]
		class_ids = range(1, (self.layer_size + 1))

		for idx, c_id in zip(indexes, class_ids):
			elected_neu = np.random.choice(self.layer_size)
			neurons[elected_neu].index(idx)
			neurons[elected_neu].class_id(c_id)

		self.setNeighbours(neurons)

		return {neuron.index: neuron for neuron in neurons}



		