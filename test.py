import numpy as np

from App.ANN.neural_package.neuronset import NeuronLayer
from App.Data.dataset_model import DataSet


def rand_training_set(dataSet, dataPartition):
	selectedData = []
	numElements = np.ceil(len(data) * dataPartition)

	while len(selectedData) < numElements:
		elected = np.random.choice(len(dataSet))
		if dataSet[elected] in selectedData:
			continue
		else:
			selectedData.append(dataSet[elected])

	return selectedData




data_set = DataSet("App/Resources/iris.data")
data_set.normalize()
new_layer = NeuronLayer(4, (4, 4), 1.75, data_set)
new_layer.normalize()

#print(new_layer.weight_matrix())

print (np.random.choice(data_set))