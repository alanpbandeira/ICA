from App.ANN.neural_module.neuron_model import Neuron
from App.ANN.neural_module.neuronset_model import NeuronLayer
from App.Data.dataset_model import DataSet

data_set = DataSet("App/Resources/iris.data")
new_layer = NeuronLayer(4, (4,4), 1, data_set)

print(new_layer.weightMatrix())
#print(new_layer[(2,2)].neighbourhood)
