from GA import problem
from GA.OptimizationModel import ga_classic

p = problem.Problem()
problem_solver = ga_classic.GA(p)

solution = problem_solver.run()

print(solution)