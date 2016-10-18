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
        self.range = self.problem.interval

    @staticmethod
    def randomPertubator(value, increase):
        if increase:
            pertubation = random.uniform(0, 0.01)
            new_value = value + pertubation
        else:
            pertubation = random.uniform(0, 0.01)
            new_value = value - pertubation

        return new_value

    def biDimEvaluate(self, current_value, candidate_value_one, candidate_value_two):
        score_list = list()

        score_list.append((self.problem.setScore(current_value), current_value))
        score_list.append((self.problem.setScore(candidate_value_one), candidate_value_one))
        score_list.append((self.problem.setScore(candidate_value_two), candidate_value_two))

        if self.problem.maximization:
            return max(score_list)[1]
        else:
            return min(score_list)[1]

    def nDimEvaluate(self, current_value, candidates):
        score_list = list()
        score_list.append((self.problem.setScore(current_value), current_value))

        for candidate in candidates:
            score_list.append((self.problem.setScore(candidate), candidate))

        if self.problem.maximization:
            return max(score_list)[1][0], max(score_list)[1][1]
        else:
            return min(score_list)[1][0], min(score_list)[1][1]

    def runBiDimOptimization(self):
        candidate_value = random.uniform(self.range[0], self.range[1])

        best_result = candidate_value
        improvement = True
        iterations = 1

        while iterations < self.max_iterations and improvement:

            candidate_value_one = self.randomPertubator(best_result, True)
            candidate_value_two = self.randomPertubator(best_result, False)

            best_candidate = self.biDimEvaluate(best_result, candidate_value_one, candidate_value_two)

            if best_candidate != best_result:
                best_result = best_candidate
            else:
                improvement = False

            best_score = self.problem.setScore(best_result)

            iterations += 1
            self.result_evolution_list.append((best_result, best_score))

        self.result_list.append((best_result, self.problem.setScore(best_result)))

        return iterations, best_result, self.problem.setScore(best_result)

    def runNDimOptimization(self):
        candidate_value_x = random.uniform(self.range[0][0], self.range[0][1])
        candidate_value_y = random.uniform(self.range[1][0], self.range[1][1])

        best_result = (candidate_value_x, candidate_value_y)
        improvement = True
        iterations = 1

        while iterations < self.max_iterations and improvement:

            candidate_value_one   = (self.randomPertubator(best_result[0], True),
                                     self.randomPertubator(best_result[1], True))
            candidate_value_two   = (self.randomPertubator(best_result[0], False),
                                     self.randomPertubator(best_result[1], False))
            candidate_value_three = (self.randomPertubator(best_result[0], True),
                                     self.randomPertubator(best_result[1], False))
            candidate_value_four  = (self.randomPertubator(best_result[0], False),
                                     self.randomPertubator(best_result[1], True))

            best_candidate = self.nDimEvaluate(best_result, (candidate_value_one, candidate_value_two,
                                                             candidate_value_three, candidate_value_four))

            if best_candidate is not best_result:
                best_result = best_candidate
            else:
                improvement = False

            best_score = self.problem.setScore(best_result)

            iterations += 1
            self.result_evolution_list.append((best_result[0], best_result[1], best_score))

        self.result_list.append((best_result[0], best_result[1], self.problem.setScore(best_result)))

        return iterations, best_result, self.problem.setScore(best_result)