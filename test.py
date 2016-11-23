import numpy as np

from App.Data.dataset_model import DataSet
from App.ANN.neural_package.neuronset import NeuronLayer
from App.ANN.network.SOM.som_trainer import SOMTrainer


def rand_training_set(dataSet, dataPartition):
	selectedData = []
	numElements = np.ceil(len(dataSet) * dataPartition)

	while len(selectedData) < numElements:
		elected = np.random.choice(len(dataSet))
		validator =	next((True for elem in selectedData if elem is dataSet[elected]), False)

		if validator:
			continue
		else:
			selectedData.append(dataSet[elected])

	return selectedData


# testDataSet = DataSet("App/Resources/iris.data")
# testDataSet.normalize()

# color dataset
flatData = np.random.randint(0, 256, 120000)
brgDataSet = flatData.reshape(200, 200, 3)
print("init data creation")
data = [brgDataSet[x][y] for x in range(brgDataSet.shape[0])
							for y in range(brgDataSet.shape[1])]
print("Color data created")

print("Selecting training data from DataSet")
# Create a DataSet object
# Select data points from data set to train the layer.
testDataSet = DataSet(raw_data=data)
trainingData = rand_training_set(testDataSet, 0.3)

# Create the neuron layer
new_layer = NeuronLayer(3, (4, 4), 1, data_type="discrete")
print ("\nUntrained layer\n", new_layer.weight_matrix())

trainer = SOMTrainer(new_layer, trainingData, 1)
trainer.start_training()
print("\nTrained layer\n", new_layer.weight_matrix())
