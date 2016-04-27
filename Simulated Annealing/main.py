from problem import Problem
from Plotter.plotter import Plotter
from simulatedAnnealing import SimulatedAnnealing
import random, math
import matplotlib.pyplot as plt

my_problem = Problem(True, (0, 1))
problem_solver = SimulatedAnnealing(my_problem, 1)

mplt = Plotter(my_problem)
mplt.samplePlot((0, 1))

fhand_hillC = open('simulatedAnnealing - data.txt', 'w')
fhand_hillC.write('Simulated Annealing Results - function a\n\n')

for x in range(10):
    k = problem_solver.run(50)
    fhand_hillC.write(str(k) + '\n')

for item in problem_solver.result_list:
    mplt.pointPlot(item[0], item[1], (0, 1))

plt.show()
