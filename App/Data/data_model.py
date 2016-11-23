import numpy as np

class DataPoint(object):
	"""
	docstring for DataPoint
	"""

	_classId = None

	def __init__(self, dataArray):
		self._dataPoints = dataArray

	def __getitem__(self, position):
		return self._dataPoints[position]

	def __setitem__(self, key, value):
		self._dataPoints[key] = value

	def __len__(self):
		return len(self._dataPoints)

	def __repr__(self):
		return str(self._dataPoints)

	@property
	def data_points(self):
		return self._dataPoints

	@data_points.setter
	def data_points(self, dataArray):
		self._dataPoints = dataArray

	@property
	def class_id(self):
		return self._classId

	@class_id.setter
	def class_id(self, newId):
		self._classId = newId
