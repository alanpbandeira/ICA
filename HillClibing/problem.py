import math


class Problem():
    """docstring for Problem"""

    def __init__(self, maximization, interval):
        self.maximization = maximization
        self.interval = interval

    @staticmethod
    def objective_function_a(x):
        element_one = -2 * math.pow(((x - 0.1) / 0.9), 2)
        element_two = math.pow(math.sin(5 * math.pi * x), 6)
        result = math.pow(2, element_one) * element_two
        return result

    @staticmethod
    def objective_function_b(x, y):
        element_one = math.exp(-(math.pow(x, 2) + math.pow(y, 2)))
        element_two = 2 * math.exp(math.pow((x - 1.7), 2) + math.pow((y - 1.7), 2))

        result = math.exp(element_one + element_two)

        return result

    @staticmethod
    def objective_function_c(x, y):
        temp = x - math.pow(y, 2)
        element_one = 100 * math.pow(temp, 2)
        element_two = math.pow((1 - x), 2)

        result = element_one + element_two

        return result

    def setScore(self, value, function):
        if function is 'a':
            return self.objective_function_a(value[0])
        elif function is 'b':
            return self.objective_function_b(value[0], value[1])
        elif function is 'c':
            return self.objective_function_c(value[0], value[1])
