import numpy as np

from ....MathLib.matrix_module import euclidian_dist

class SOMClassifier(object):
    """docstring for Classifier."""
    def __init__(self, dataSet, neuronLayer):
        self.dataSet = dataSet
        self.neuronLayer = neuronLayer

    def classify(self):
        for data in self.dataSet:
            currentDist = None
            for neuron in self.neuronLayer:
                candidateDist = euclidian_dist(data.data_points, neuron.weights)
                if currentDist is None or candidateDist < currentDist:
                    currentDist = candidateDist

            data.class_id = nueron.class_id
