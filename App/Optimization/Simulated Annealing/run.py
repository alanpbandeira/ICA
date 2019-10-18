from problem import Problem
from Plotter.plotter import Plotter
from simulatedAnnealing import SimulatedAnnealing
import matplotlib.pyplot as plt


my_problem = Problem(True, (0, 1))
problem_solver = SimulatedAnnealing(my_problem, 0.001)

initial_temperature = problem_solver.run(100, 1, True)

print (initial_temperature)

mplt = Plotter(my_problem)
mplt.samplePlot((0, 1))

fhand_hillC = open('simulatedAnnealing - data.txt', 'w')
fhand_hillC.write('Simulated Annealing Results - function a\n\n')

for x in range(10):
    k = problem_solver.run(100, initial_temperature, False)
    fhand_hillC.write(str(k) + '\n')

for item in problem_solver.result_list:
    mplt.pointPlot(item[0], item[1], (0, 1))

plt.show()
