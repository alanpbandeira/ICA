import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


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
    @Parameter: x_value -> Array of x values.
    @Parameter:
    """

    def __init__(self, problem):
        self.problem = problem
        self.axis_range = self.problem.interval

    def samplePlot(self, delta, function):
        if len(self.axis_range) is 1:
            x_axis = np.arange(self.axis_range[0][0], self.axis_range[0][1], delta)

            y_axis = np.array([self.problem.setScore(x, 'a')] for x in x_axis)

            plt.plot(x_axis, y_axis, 'b')
        elif len(self.axis_range) is 2:
            x_axis = np.arange(self.axis_range[0][0], self.axis_range[0][1], delta)
            y_axis = np.arange(self.axis_range[1][0], self.axis_range[1][1], delta)

            X, Y = np.meshgrid(x_axis, y_axis)

            z_axis = np.array([self.problem.setScore((x,y), function) for x, y in zip(np.ravel(X), np.ravel(Y))])

            Z = z_axis.reshape(X.shape)

            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='b')

    def pointPlot(self, x_value, y_value):
        plt.plot(x_value, y_value, 'ro')
