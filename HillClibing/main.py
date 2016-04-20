from problem import Problem
from hillClibing import HillClibing
from iteratedHillClibing import IteratedHillClibing
from Plotter.plotter import Plotter
import random, math
import matplotlib.pyplot as plt


my_problem = Problem(True, (0,1))
problem_solver  = HillClibing(1000, my_problem)
iterated_solver = IteratedHillClibing(40, problem_solver)

mplt = Plotter(my_problem)
mplt.samplePlot((0,1))

#fhand_hillC = open('hillClibing - data.txt', 'w')
#fhand_hillC.write('HillClibing Results - function a\n\n')

#for x in range(10):
#	k = problem_solver.run()
#	fhand_hillC.write(str(k) + '\n')

#for item in problem_solver.result_list:
#	mplt.pointPlot(item[0], item[1], (0,1))

fhand_IHillC = open('iteratedHillClibing - data.txt', 'w')
fhand_IHillC.write('Iterated HillClibing Results - function a\n\n')

for x in range(10):
	k = iterated_solver.run()
	fhand_IHillC.write(str(k) + '\n')

for item in iterated_solver.result_list:
	mplt.pointPlot(item[0], item[1], (0,1))

plt.show()