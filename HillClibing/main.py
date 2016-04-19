from problem import Problem
from hillClibing import HillClibing
from iteratedHillClibing import IteratedHillClibing
from Plotter.plotter import Plotter as mplt
import random, math

my_problem = Problem(True, (0,1))
problem_solver  = HillClibing(1000, my_problem)
iterated_solver = IteratedHillClibing(100, problem_solver)


for x in range(10):
	print (iterated_solver.run())

mplt.samplePlot(my_problem.interval, (0,1))