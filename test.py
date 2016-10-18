from App.ANN.neural_module.neuron_model import Neuron

import numpy as np


data = np.array([1,1,1,1,1,2])

a = Neuron(n_weights=10, value_range=(1,10))
a.setNorm()

print (a.norm, a.weights)