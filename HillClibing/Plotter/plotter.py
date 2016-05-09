import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Plotter:
    """
    --
    @method: __init__ -> Initialize the object based on received parameters.
    @Param: problem -> Represents the optimization problem to be plotted.
    --

    --
    @Method: samplePlot -> Draws the function graph for a generic view.
    @Parameter: delta -> Represents the difference between values for the numpy array creation.
    @Parameter: function -> Represents the function to be plotted.
    --

    --
    @Method: pointPlot -> Plot the optimization values over the function graph.
    @Parameter: plot_array -> Tuples of arrays to be plotted.
    @Parameter:
    """

    def __init__(self, problem):
        self.problem = problem
        self.axis_range = self.problem.interval

    def samplePlot(self, delta):
        if not isinstance(self.axis_range[0], tuple):
            x_axis = np.arange(self.axis_range[0], self.axis_range[1], delta)
            y_axis = np.array([self.problem.setScore(x) for x in x_axis])

            plt.plot(x_axis, y_axis, 'b')
        else:
            x_axis = np.arange(self.axis_range[0][0], self.axis_range[0][1], delta)
            y_axis = np.arange(self.axis_range[1][0], self.axis_range[1][1], delta)

            X, Y = np.meshgrid(x_axis, y_axis)

            z_axis = np.array([self.problem.setScore((x, y)) for x, y in zip(np.ravel(X), np.ravel(Y))])

            Z = z_axis.reshape(X.shape)

            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='b')

    def pointPlot(self, plot_array):
        if len(plot_array) is 2:
            plt.plot([plot_array[0]], [plot_array[1]], 'ro')
        elif len(plot_array) is 3:
            plt.plot([plot_array[0]], [plot_array[1]], [plot_array[2]], 'ro')
