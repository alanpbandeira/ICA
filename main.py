from problem import Problem
from hillClibing import HillClibing
import random, math

my_problem = Problem(True, (0,1))
problem_solver = HillClibing(1000, my_problem)

for x in range(10):
	print (problem_solver.run())