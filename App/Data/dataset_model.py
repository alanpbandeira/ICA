import numpy as np

from .data_model import DataPoint
from ..MathLib.matrix_module import vector_norm 


class DataSet(object):
	"""
	docstring for DataSet
	"""

	def __init__(self, file_name=None, raw_data=None):
		if file_name is not None and raw_data is None:
			self._data = np.array(self.csvImport(file_name))
		elif file_name is None and raw_data is not None:
			self._data = raw_data
		else:
			raise ("Only one model of creating datasets can be used!")

	def __len__(self):
		return len(self._data)

	def __getitem__(self, position):
		return self._data[position]

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
		"""
		todo
		"""
		return np.array([element.data_points for element in self._data])

	def normalize(self):
		"""
		todo
		"""
		for index in range(len(self._data)):
			normalized = vector_norm(self._data[index])
			self._data[index] = normalized

	@property
	def data(self):
		return self._data