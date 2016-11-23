import numpy as np

from ...MathLib.matrix_module import vector_mod
from ...MathLib.gaussian_module import vect_gaussian_func


class Neuron(object):
    """
	Docstring for Neuron
	"""

    #
    # PROTECTED ATTRIBUTES
    #

    _neighbourhood = None
    _class_id = None
    _index = None


    #
    # DUNDER METHODS
    #

    def __init__(self, weight_list=None, size=None, data_type="continuous"):
        """
        Class that defines the Neuron object. If weights is given the others

        :param weight_list: 1D numpy array of numeric values, if no data is
        passed the neuron will be set with an array of random values.

        :param size: Number of weight that will compound the neuron randomly generated.
        :param data_type: 
        """
        if weight_list is not None:
        	self._weights = weight_list
        else:
            if data_type == "discrete":
                self._weights = np.random.randint(0, 10, size)
            elif data_type == "continuous":
                self._weights = np.random.uniform(0, 1, size)
            else:
                raise ValueError("Data type should be continuous or discrete")

        self._norm = vector_mod(self._weights)

    def __len__(self):
    	return len(self._weights)

    def __getitem__(self, index):
    	return self._weights[index]

    def __setitem__(self, key, value):
    	self._weights[key] = value

    def __str__(self):
    	return str(self._weights)
    
    #
    # CLASS METHODS
    #

    def actv_function(self, data, learningRate, winner=False):
        """
        Activation function for the standart competitive learning mechanism.
        
        :param data: Data point from the training data.
        
        :param learningRate: Constant that defines the intensity of the change
        that the neuron will suffer from the learning process.

        :param winner: Switch that sets if the neuron beeing updated is winner
        or is a neighbour of the winner.

        """
        
        if winner:
            self._weights = self._weights + (learningRate * (data - self._weights))
        else:
            self._weights = self._weights + (learningRate / 2 * (data - self._weights))

    def gaussian_actv_function(self, data, learningRate, sigma, winner=True, winnerNeuron=None):
        """
        Activation function for the gaussian competitive learning mechanism.
        
        :param data: Data point from the training data.
        
        :param learningRate: Constant that defines the intensity of the change
        that the neuron will suffer from the learning process.

        :param sigma: standart deviation.

        :param winner: Switch that sets if the neuron beeing updated is winner
        or is a neighbour of the winner.

        """

        if winner:
            self._weights = self._weights + (learningRate * (data - self._weights))
        else:
            learningMod = vect_gaussian_func(winnerNeuron, learningRate, self._weights, sigma)
            self._weights = self.weights + learningMod * (data - self._weights)

    #
    # PROPERTIES
    #

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, value):
        self._weights = value

    @property
    def norm(self):
        return self._norm

    @norm.setter
    def norm(self, value):
        self._norm = value

    @property
    def neighbourhood(self):
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, array):
        self._neighbourhood = array

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):
        self._class_id = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value