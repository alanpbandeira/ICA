import numpy as np

from App.ANN.neural_package.neuron_set import NeuronLayer


class SOMTrainer(object):
    """docstring for SOMTrainer"""

#
# DUNDER METHODS
#

    def __init__(self, layer, data, learning_rate):
        self._training_data = data
        self._neuron_layer = layer
        self._learning_rate = learning_rate

    #
    # CLASS METHODS
    #

    def start_training(self, normalized=True):
        """
        @param: normalized:
        """

        print("Starting SOM training")

        # Used to keep track if a significant variation is still
        # happening in the learning process.
        variation_tracker = [1] * len(self.neuron_layer)
        epochs = 0

        if normalized:
            self._neuron_layer.normalize()
            self._training_data


#
# Properties
#

    @property
    def training_data(self):
        return self._training_data

    @training_data.setter
    def function(self, data):
        self._training_data = data

    @property
    def neuron_layer(self):
        return self._neuron_layer

    @neuron_layer.setter
    def neuron_layer(self, layer):
        self._neuron_layer = layer

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, rate):
        self._learning_rate = rate
