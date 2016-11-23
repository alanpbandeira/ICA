import numpy as np

from ...neural_package.neuronset import NeuronLayer
from ....MathLib.matrix_module import euclidian_dist

class SOMTrainer(object):
    """docstring for SOMTrainer"""

    #
    # DUNDER METHODS
    #

    _trainingEpochs = []

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

    def start_training(self, normalized=False):
        """
        Perform training to the neuron set of the ANN

        :param normalized: Boolean value that is set to True if neuron weights
        and training data should be normalized, or False otherwise.
        """

        print("\n[Starting " + self.neuronset.network_model() + " training]\n")

        # Used to keep track if a significant variation is still
        # happening in the learning process.
        variationTracker = np.array([1] * len(self.neuronset))
        layerKeys = list(self._neuronset.layer_map.keys())
        epochs = 0

        if normalized:
            self._neuronset.normalize()
            self._training_data.normalize()

        while variationTracker.any():
            currentNeuronSet = self._neuronset.layer_map.copy().items()

            for data in self._training_data:
                winnerDist = None
                winner = None

                # debug copy
                # d_copy = self._neuronset.weight_matrix().copy()

                for layerIndex, neuron in sorted(currentNeuronSet):
                    candidateDist = euclidian_dist(data, neuron.weights)
                    if winnerDist is None or candidateDist < winnerDist:
                        winnerDist = candidateDist
                        winner = layerIndex
                    else:
                        continue

                self._neuronset[winner].actv_function(data, self._learningRate, winner=True)


                for neighbour in self._neuronset[winner].neighbourhood:
                    self._neuronset[neighbour].actv_function(data, self._learningRate)

                # debug print and break
                # print ("\n\n", self._neuronset[winner].neighbourhood)
                # print (self._neuronset.weight_matrix() - d_copy)
                # break

                epochs += 1

            # Update the variatonTracker
            for layerIndex, neuron in currentNeuronSet:
                checker = self._neuronset[layerIndex].weights - neuron.weights
                if checker.any():
                    variationTracker[layerKeys.index(layerIndex)] = 1
                else:
                    variationTracker[layerKeys.index(layerIndex)] = 0


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
