from problem import Problem
from Plotter.plotter import Plotter
from beamSearch import BeamSearch
import random, math
import matplotlib.pyplot as plt

my_problem = Problem(True, (0, 1))
problem_solver = BeamSearch(my_problem, 100, 0.2)

mplt = Plotter(my_problem)
mplt.samplePlot((0, 1))

fhand_hillC = open('Beam Search - data.txt', 'w')
fhand_hillC.write('Beam Search Results - function a\n\n')

for x in range(10):
    k = problem_solver.run(50)
    fhand_hillC.write(str(k) + '\n')

for item in problem_solver.result_list:
    mplt.pointPlot(item[0], item[1], (0, 1))

plt.show()
