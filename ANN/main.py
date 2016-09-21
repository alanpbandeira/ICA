import numpy as np
import math

def csvImport(file_name):
	fhand = open(file_name, 'r')
	raw_data = [",".join(line.split(',')[:4]) for line in fhand]
	raw_data = [float(element) for element in ",".join(raw_data).split(",")]
	data = np.array(raw_data).reshape(math.ceil(len(raw_data) / 4), 4)

	return data

data = csvImport("iris-data.csv")

