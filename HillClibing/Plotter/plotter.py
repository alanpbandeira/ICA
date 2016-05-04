import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


class Plotter():
    """docstring for Plotter"""

    def __init__(self, problem):
        self.problem = problem

    def samplePlot(self, delta, function, dimensions):
        if dimensions is 2:
            range = self.problem.interval
            x_axis = np.arange(range[0], range[1], delta)

            y_axis = np.array([self.problem.setScore(x, 'a')] for x in x_axis)

            plt.plot(x_axis, y_axis, 'b')
        elif dimensions is 3:
            range = self.problem.interval
            x_axis = y_axis = np.arange(range[0], range[1], delta)

            X, Y = np.meshgrid(x_axis, y_axis)

            z_axis = np.array([self.problem.setScore((x,y), function) for x, y in zip(np.ravel(X), np.ravel(Y))])

            Z = z_axis.reshape(X.shape)

            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='b')





    def pointPlot(self, x_value, y_value, y_interval):
        plt.plot(x_value, y_value, 'ro')
        plt.axis([self.problem.interval[0], self.problem.interval[1], y_interval[0], y_interval[1]])
