from App.ANN.neural_package.neuron import Neuron
from App.ANN.neural_package.neuronset import NeuronLayer
from App.Data.dataset_model import DataSet

data_set = DataSet("App/Resources/iris.data")
data_set.normalize()
new_layer = NeuronLayer(4, (4, 4), 1, data_set)
new_layer.normalize()

print(new_layer.weightMatrix())
print(new_layer[(2, 2)].neighbourhood)

# print (type(data_set[:5]))
