import numpy as np

from App.ANN.neural_package.neuron_set import NeuronLayer


class SOMTrainer(object):
    """docstring for SOMTrainer"""

#
# DUNDER METHODS
#

    def __init__(self, layer, data, learning_rate):
        self._training_data = data
        self._neuronset = layer
        self._learning_rate = learning_rate

    #
    # CLASS METHODS
    #

    def start_training(self, normalized=True):
        """
            Perform training to the neuron set of the ANN

            :param normalized: Boolean value that is set to True if neuron weights
            and training data should be normalized, or False otherwise.
        """

        print("Starting " + self.neuronset.network_model() + " training")

        # Used to keep track if a significant variation is still
        # happening in the learning process.
        variation_tracker = [1] * len(self.neuronset)
        epochs = 0

        if normalized:
            self._neuronset.normalize()
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
    def neuronset(self):
        return self._neuronset

    @neuronset.setter
    def neuronset(self, layer):
        self._neuronset = layer

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, rate):
        self._learning_rate = rate
