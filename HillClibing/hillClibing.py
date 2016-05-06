import random


class HillClibing:
    """

    The @return pattern for the solution is a tuple in the
    following model: (number of iterations, best result, best result score)

    """

    result_list = list()
    result_evolution_list = list()

    def __init__(self, max_iterations, problem):
        self.max_iterations = max_iterations
        self.problem = problem

    @staticmethod
    def randomPertubator(value, increase):
        if increase:
            pertubation = random.uniform(0, 0.01)
            new_value = value + pertubation
        else:
            pertubation = random.uniform(0, 0.01)
            new_value = value - pertubation

        return new_value

    def evaluate(self, current_value, candidate_value_one, candidate_value_two):
        score_list = list()

        score_list.append((self.problem.setScore(current_value), current_value))
        score_list.append((self.problem.setScore(candidate_value_one), candidate_value_one))
        score_list.append((self.problem.setScore(candidate_value_two), candidate_value_two))

        if self.problem.maximization:
            return max(score_list)[1]
        else:
            return min(score_list)[1]

    def run(self):
        candidate_value = random.uniform(self.problem.interval[0], self.problem.interval[1])

        best_result = candidate_value
        improvement = True
        iterations = 1

        while iterations < self.max_iterations and improvement:

            candidate_value_one = self.randomPertubator(best_result, True)
            candidate_value_two = self.randomPertubator(best_result, False)

            best_candidate = self.evaluate(best_result, candidate_value_one, candidate_value_two)

            if best_candidate != best_result:
                best_result = best_candidate
            else:
                improvement = False

            best_score = self.problem.setScore(best_result)

            iterations += 1
            self.result_evolution_list.append((best_result, best_score))

        self.result_list.append((best_result, self.problem.setScore(best_result)))

        return iterations, best_result, self.problem.setScore(best_result)
