from App.ANN.neural_package.neuron import Neuron
from App.ANN.neural_package.neuronset import NeuronLayer
from App.Data.dataset_model import DataSet

data_set = DataSet("App/Resources/iris.data")
data_set.normalize()
new_layer = NeuronLayer(4, (4, 4), 1.75, data_set)
new_layer.normalize()

print(new_layer.weightMatrix())