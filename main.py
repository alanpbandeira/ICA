#from Data.csv_module.dataset_model import DataSet
import numpy as np
#my_data = DataSet('Resources/iris.data')
from MathLib.matrix_module import matrix_model as mm

#a = np.array([10, 20, 5, 15])
a = np.matrix([10, 20, 5, 15])
b = np.matrix([[1,1], [2,3], [2,5], [8,1]])

print (np.shape(a))
print (np.shape(b))

k = mm.linearCombination(a, b)

print(k, np.shape(k))
