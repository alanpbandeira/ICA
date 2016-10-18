import numpy as np

class DataPoint(object):
	"""
	docstring for DataPoint
	"""
	
	def __init__(self, data_array):
		self._data_points = data_array
		self._class_id = None

	def __getitem__(self, position):
		return self._data_points[position]

	def __setitem__(self, key, value):
		self._data_points[key] = value

	def __len__(self):
		return len(self._data_points)

	def __repr__(self):
		return str(self._data_points)

	@property
	def data_points(self):
		return self._data_points

	@data_points.setter
	def data_points(self, data_array):
		self._data_points = data_array
