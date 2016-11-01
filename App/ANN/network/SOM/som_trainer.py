import numpy as np

from App.ANN.neural_package.neuron_set import NeuronLayer

class SOMTrainer(object):
	"""docstring for SOMTrainer"""
	def __init__(self, layer, data, learning_rate):
		self.neuron_layer = layer
		self.learning_rate = data
		self.training_data = learning_rate

	def function(self, normalized=True):

		# Used to keep track if a significant variation is still
		# happeninig in the learning process.
		variation_tracker = [1] * len(self.neuron_layer)
		epochs = 0		

		if normalized:
			self.neuron_layer.normalize()

		
