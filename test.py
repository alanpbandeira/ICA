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


testDataSet = DataSet("App/Resources/iris.data")
testDataSet.normalize()

trainingData = rand_training_set(testDataSet, 0.3)

new_layer = NeuronLayer(4, (4, 4), 1.75)
new_layer.normalize()

#print("Untrained data:\n", new_layer.weight_matrix(), "\n\n")

trainer = SOMTrainer(new_layer, trainingData, 1)

trainer.start_training()

print(new_layer.weight_matrix())