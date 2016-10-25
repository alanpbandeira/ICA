import numpy as np

from .neuron_model import Neuron


class LayerBuilder(object):
	"""docstring for Builder"""
	
		
#
#	CLASS METHODS
#

	@staticmethod
	def neuronsFromData(self, data_set, size):
		"""
		Select data points to compound the neuronset

		@param: data_set: DataSet Object or array of data Objects.
		"""

		if len(data_set) == size:
			candidates = data_set
		elif len(data_set) < size:
			return "Insuficient Data"
		else:
			candidate = []
			count = 0
			while count < size:
				candidate = np.random.choice(data_set)
				if candidate in candidates:
					continue
				else:
					candidates.append(candidate)
					count += 1

		return [Neuron(candidate.data) for candidate in candidates]

	@staticmethod	
	def genLayerIndexes(self, size, dimensions):
		"""
		Create matrix-like indexes to the layer with linear complexity.
		"""

		indexes = []

		if size < 1:
			raise ValueError("Impossible to create zero-sided layer")

		x_counter = 1
		y_counter = 1

		while x_counter <= dimensions[0]:
			if y_counter <= dimensions[1]:
				indexes.append([x_counter, y_counter])
				y_counter += 1
			else:
				x_counter += 1

		return indexes

	@staticmethod
	def setNeighbours(self, neurons, radius):
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
					if euclidianDist(p_one, p_two) <= radius:
						candidates.append(candidate.index)

			neurons[index].neighbourhood = candidate.copy()


	@staticmethod
	def build(self, size, dimensions, radius):
		"""
		"""

		indexes = self.genLayerIndexes(size, dimensions)
		neurons = [Neuron(neuron_size) for x in range(size)]
		class_ids = range(1, (size + 1))

		for idx, c_id in zip(indexes, class_ids):
			elected_neu = np.random.choice(size)
			neurons[elected_neu].index(idx)
			neurons[elected_neu].class_id(c_id)

		self.setNeighbours(neurons, radius)

		