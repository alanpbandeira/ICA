import numpy as np

from .data_model import DataPoint


class DataSet(object):
	"""
	docstring for DataSet
	"""

	def __init__(self, file_name):
		self._data = np.array(self.csvImport(file_name))

	def __len__(self):
		return len(self._data)

	def __getitem__(self, position):
		return self._data[position].data_points

	def __setitem__(self, key, value):
		self._data[key] = value

	def __repr__(self):
		return str(self._data)

	@staticmethod
	def csvImport(file_name):
		fhand = open(file_name, 'r')
		raw_data = [[float(value) for value in line.split(",")] for line in fhand]
		return [DataPoint(np.array(line)) for line in raw_data]

	def dataMatrix(self):
		return np.array([element.data_points for element in self._data])