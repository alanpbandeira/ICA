import numpy as np


class DataIndividual(object):
	"""docstring for DataIndividual"""
	def __init__(self, data_point):
		"""
		@param: data_point :: 1D numpy array of float point values
		"""
		self.data_point = data_point
		self.class_id = None
