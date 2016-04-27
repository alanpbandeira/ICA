from problem import Problem
import random, math


class SimulatedAnnealing():
    """docstring for SimulatedAnnealing"""

    result_list = list()

    def __init__(self, task_problem, final_temperature):
        self.problem = task_problem
        self.final_temperature = final_temperature

    def coolingFunction(self, temperature, init_temperature, max_epoch):
        alpha_exponent = 1 / (max_epoch - 1)
        alpha = math.pow((self.final_temperature / init_temperature), alpha_exponent)

        new_temperature = alpha * temperature

        return new_temperature

    @staticmethod
    def randomPertubator(value):
        if random.uniform(0, 1) > 0.5:
            increase = True
        else:
            increase = False

        if increase:
            pertubation = random.uniform(0, 0.01)
            new_value = value + pertubation
        else:
            pertubation = random.uniform(0, 0.01)
            new_value = value - pertubation

        return new_value

    def run(self, max_iterations, initial_temperature, trial):
        candidate_list = list()
        down_hill_temperature_list = list()

        temperature = initial_temperature
        interval = self.problem.interval

        best_value = random.uniform(interval[0], interval[1])
        best_score = self.problem.setScore(best_value)
        epochs = 1
        jump_count = 0

        while epochs < max_iterations:
            for x in range(10):
                candidate_value = self.randomPertubator(best_value)
                candidate_score = self.problem.setScore(candidate_value)
                candidate_list.append((candidate_score, candidate_value))

            for candidate in candidate_list:
                score_variation = best_score - candidate[0]

                if score_variation < 0:
                    best_value = candidate[1]
                    best_score = candidate[0]
                    cooling_factor = -score_variation / temperature
                elif math.exp(cooling_factor) <= random.uniform(0, 1):
                    best_value = candidate[1]
                    best_score = candidate[0]
                    jump_count += 1
                    down_hill_temperature_list.append(candidate_score)
                    cooling_factor = -score_variation / temperature

            temperature = self.coolingFunction(temperature, initial_temperature, max_iterations)
            epochs += 1

        if trial:
            acceptance_probability = len(down_hill_temperature_list) / epochs
            down_hill_average_score = sum(down_hill_temperature_list) / len(down_hill_temperature_list)

            trial_temperature = down_hill_average_score / math.log(acceptance_probability)

            return trial_temperature
        else:
            self.result_list.append((best_value, best_score))
            return epochs, best_value, best_score
