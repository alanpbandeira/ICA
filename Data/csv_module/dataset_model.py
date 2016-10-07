import numpy as np
import numbers
from .data_model import DataIndividual


class DataSet(object):
	"""docstring for DataSet"""
	def __init__(self, file_name):
		raw_data = self.csvImport(file_name)
		self._data = [DataIndividual(np.array(line)) for line in raw_data]

	def __len__(self):
		return len(self._data)

	def __getitem__(self, position):
		return self._data[position]

	@staticmethod
	def csvImport(file_name):
		fhand = open(file_name, 'r')
		raw_data = [[float(value) for value in line.split(",")] for line in fhand]
		return raw_data
