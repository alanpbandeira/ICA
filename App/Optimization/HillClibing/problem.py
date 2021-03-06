import math
import numpy as np
# TO TEST!!!


class Problem:
    """

    ---
    __init__ -> initialize the problem object using the given parameters.
    @:parameter maximization: Set the problem as a maximization or minimization problem.
    @:parameter interval: Set the optimization function interval.
    @:parameter function: Select the function to be used.
    ---

    ---
    setScore -> Calculate the score using the selected function.
    @:parameter value: Represents the values to be used in the function.
    @:type double/float for two dimensional function.
    @:type n_size tuple for a n_dimensional function.
    ---

    """

    def __init__(self, maximization, interval, function):
        self.maximization = maximization
        self.interval = interval
        self.function = function

    @staticmethod
    def objective_function_a(x):
        element_one = -2 * math.pow(((x - 0.1) / 0.9), 2)
        element_two = math.pow(math.sin(5 * math.pi * x), 6)
        result = math.pow(2, element_one) * element_two
        return result

    @staticmethod
    def objective_function_b(x, y):
        element_one = np.exp(-(np.power(x, 2) + np.power(y, 2)))
        a = np.power((x - 1.7), 2)
        b = np.power((y - 1.7), 2)
        element_two = 2 * np.exp(a + b)

        result = element_one + element_two

        return result

    @staticmethod
    def objective_function_c(x, y):
        temp = x - math.pow(y, 2)
        element_one = 100 * math.pow(temp, 2)
        element_two = math.pow((1 - x), 2)

        result = element_one + element_two

        return result

    def setScore(self, value):
        if self.function is 'a':
            return self.objective_function_a(value)
        elif self.function is 'b':
            return self.objective_function_b(value[0], value[1])
        elif self.function is 'c':
            return self.objective_function_c(value[0], value[1])
