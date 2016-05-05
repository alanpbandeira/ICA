from problem import Problem
from hillClibing import HillClibing
from iteratedHillClibing import IteratedHillClibing
from Plotter.plotter import Plotter
import random, math
import matplotlib.pyplot as plt

my_problem = Problem(True, (0, 1))
problem_solver = HillClibing(1000, my_problem)
iterated_solver = IteratedHillClibing(30, problem_solver)

mplt = Plotter(my_problem)
mplt.samplePlot((0, 1))

# fhand_hillC = open('hillClibing - data.txt', 'w')
# fhand_hillC.write('HillClibing Results - function a\n\n')

# Execute Random Hill Clibing 10 times and export
# the optimun foud at each iteration
#
# for x in range(10):
#	k = problem_solver.run()
#	fhand_hillC.write(str(k) + '\n')

# Plot the process of otimization of a single
# Hll Clibing iteration, uncoment to use
#
# for item in problem_solver.result_list:
#	mplt.pointPlot(item[0], item[1], (0,1))

# Plot the best results of 10 iterations of the
# Hill Clibing
# uncoment to use
#
# for item in problem_solver.result_list:
#	mplt.pointPlot(item[0], item[1], (0,1))

fhand_IHillC = open('iteratedHillClibing - data.txt', 'w')
fhand_IHillC.write('Iterated HillClibing Results - function a\n\n')

# Execute Iterated Hill Clibing 10 times and export
# the optimun foud at each iteration
#
for x in range(10):
    k = iterated_solver.run()
    fhand_IHillC.write(str(k) + '\n')

for item in iterated_solver.result_list:
    mplt.pointPlot(item[0], item[1], (0, 1))

plt.show()
