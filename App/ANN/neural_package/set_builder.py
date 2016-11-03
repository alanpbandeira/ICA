import numpy as np

from .neuron import Neuron
from ...MathLib.matrix_module import *


class LayerBuilder(object):
    """docstring for Builder"""

    def __init__(self, layer_size, layer_dimensions, layer_radius):
        self.layer_radius = layer_radius
        self.layer_dimensions = layer_dimensions
        self.layer_size = layer_size

#
# CLASS METHODS
#

    def neuronsFromData(self, data_set):
        """
        Select data points to compound the neuronset.

        @param: data_set: DataSet Object or array of data Objects.
        @return: list(): List DS of Neuron objects using data objects as models.
        """

        if len(data_set) == self.layer_size:
            candidates = data_set
        elif len(data_set) < self.layer_size:
            return "Insuficient Data"
        else:
            candidates = []
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

        @return: indexes: List of tuples of layer indexes (row, columns).
        """

        indexes = []

        if self.layer_size < 1:
            raise ValueError("Impossible to create zero-sided layer")

        x_counter = 1
        y_counter = 1

        while x_counter <= self.layer_dimensions[0]:
            if y_counter <= self.layer_dimensions[1]:
                indexes.append((x_counter, y_counter))
                y_counter += 1
            else:
                y_counter = 1
                x_counter += 1

        return indexes

    def setNeighbours(self, neurons):
        """
        Set the neighbourhood for the given neurons using the layer_radius attribute.

        @param: neurons: Array of Neuron Objects.
        """

        for neuron_idx in range(len(neurons)):
            candidates = []

            for candidate in neurons:
                if candidate is neurons[neuron_idx]:
                    continue
                else:
                    p_one = np.array(neurons[neuron_idx].index)
                    p_two = np.array(candidate.index)
                    if euclidianDist(p_one, p_two) <= self.layer_radius:
                        candidates.append(candidate.index)

            neurons[neuron_idx].neighbourhood = candidates.copy()

    def build(self, neuron_size, data_set=None):
        """
        Creates the maping [neuron_index: Neuron] using the layer parameters
        of the builder class. Each neuron is set with an index, a class_id	and a list of indexes for neighbourhood.

        @param: neuron_size: Numbers of weights of a Neuron.
        @return: dict(): Dictionary DS with nuron_index as key a Neuron obj
        as data.
        """

        indexes = self.genLayerIndexes()
        layer_ids = list(range(1, (self.layer_size + 1)))

        if data_set is not None:
            neurons = [Neuron(weight_list=data) for data in data_set[0:self.layer_size]]
        else:
            neurons = [Neuron(size=neuron_size) for x in range(self.layer_size)]

        for idx in range(len(neurons)):
            layer_index = np.random.choice(len(indexes))
            class_index = np.random.choice(len(layer_ids))
            neurons[idx].index = indexes[layer_index]
            neurons[idx].class_id = layer_ids[class_index]
            del indexes[layer_index]
            del layer_ids[class_index]

        self.setNeighbours(neurons)

        return {neuron.index: neuron for neuron in neurons}
