import numpy as np
from App.ANN.neural_module.neuronset_model import NeuronLayer
from App.Data.dataset_model import DataSet

my_set = DataSet('App/Resources/iris.data')
neurons = NeuronLayer()


print (my_set.valuedMatrix())
#print (my_set[0].data)