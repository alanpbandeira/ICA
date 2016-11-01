import numpy as np
import matplotlib.pyplot as plt


def comparative_plot(init_data, classificaton_data, centroids):
	"""
	@Info: Comparative plot of the same data set 
		   before and after classification process.

	@param: init_data :: Initial data set as a 2-DIM Numpy Array.
	
	@param: classification_data :: List structure with classes 
			integers values sorted to match the init_data sorting.

	@param: centroids :: Data set centroids as a 2-DIM Numpy Array.
	"""
	
	fig = plt.figure(1)
	
	# Plotting unclassified data
	plt.subplot(211)
	plt.scatter(init_data[:, 0], init_data[:, 1], s=50)
	plt.tight_layout()
	plt.title("Unclassified Data Set")
	plt.xlabel("Feature 1")
	plt.ylabel("Feature 2")

	# Plotting classified data.
	plt.subplot(212)
	plt.scatter(init_data[:, 0], init_data[:, 1], c=classificaton_data, s=50, cmap='rainbow')
	plt.title("Classified Data Set")
	plt.xlabel("Feature 1")
	plt.ylabel("Feature 2")
	plt.tight_layout()
	# Plotting centroids
	plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=50)
	

	plt.show()