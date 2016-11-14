import numpy as np

from ...neural_package.neuronset import NeuronLayer
from ....MathLib.matrix_module import euclidian_dist

class SOMTrainer(object):
    """docstring for SOMTrainer"""

    #
    # DUNDER METHODS
    #

    self._trainingEpochs = []

    def __init__(self, layer, data, learningRate):
        """
        :param layer: Layer Map of neurons.
        :param data: Data sample to be used as a training set.
        :param learningRate: Learning influence over the neural layer. 
        """
        self._training_data = data
        self._neuronset = layer
        self._learningRate = learningRate

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
        variationTracker = [1] * len(self.neuronset)
        layerKeys = self._neuronset.keys()
        epochs = 0

        if normalized:
            self._neuronset.normalize()
            self._training_data.normalize()

        while variationTracker.any():
            for data in self._training_data:
                currentNeuronSet = self._neuronset.items()
                winnerDist = None
                winner = None

                for layerIndex, neuron in currentNeuronSet:
                    candidateDist = euclidian_dist(data, neuron.weights)
                    if winnerDist is None or candidateDist < winnerDist:
                        winnerDist = candidateDist
                        winner = layerIndex
                    else:
                        continue

                self._neuronset[winner].act_function(data, learningRate, winner=True)

                for neighbour in self._neuronset[winner].neighbourhood:
                    self._neuronset[neighbour].act_function(data, learningRate)

                # Update the variatonTracker
                for layerIndex, neuron in currentNeuronSet:
                    if self._neuronset[layerIndex] != neuron:
                        continue
                    else:
                        variationTracker[layerKeys.index(layerIndex)] = 0

                epochs += 1

            self._trainingEpochs.append(epochs)


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
        return self._learningRate

    @learning_rate.setter
    def learning_rate(self, rate):
        self._learningRate = rate

    @property
    def training_epochs(self):
        return self._trainingEpochs