from problem import Problem
from hillClibing import HillClibing
from iteratedHillClibing import IteratedHillClibing
from Plotter.plotter import Plotter
import matplotlib.pyplot as plt

my_problem = Problem(True, ((-2, 4), (-2, 4)), 'b')
problem_solver  = HillClibing(100, my_problem)
iterated_solver = IteratedHillClibing(30, problem_solver)

mplt = Plotter(my_problem)
mplt.samplePlot(0.1)

"""

fhand_hillC = open('hillClibing - data.txt', 'w')
fhand_hillC.write('HillClibing Results - function b\n\n')

# Execute Random Hill Clibing 10 times and export
# the optimun foud at each iteration

for x in range(10):
    k = problem_solver.runNDimOptimization()
    fhand_hillC.write(str(k) + '\n')


# Plot the process of otimization of a single
# Hll Clibing iteration, uncoment to use

#for item in problem_solver.result_evolution_list:
#    mplt.pointPlot(item)



# Plot the best results of 10 iterations of the
# Hill Clibing
# uncoment to use

for item in problem_solver.result_list:
    mplt.pointPlot(item)

"""

#"""

fhand_IHillC = open('iteratedHillClibing - data.txt', 'w')
fhand_IHillC.write('Iterated HillClibing Results - function b\n\n')

# Execute Iterated Hill Clibing 10 times and export
# the optimun foud at each iteration
#
for x in range(10):
    k = iterated_solver.runNDimOptimization()
    fhand_IHillC.write(str(k) + '\n')


for item in iterated_solver.result_list:
    mplt.pointPlot(item)

#"""

plt.show()
