from ICA.GA.IndividualModel.individual import Individual


class Population:

    __similarity = None
    __population_fitness = None

    def __init__(self, individual_list=None, rand=False, size=100):
        self.__size = size

        if rand:
            self.individual_list = [Individual() for count in range(self.__size)]
        else:
            self.individual_list = individual_list

    @staticmethod
    def similarityCalc(self):
        """TODO"""
        pass

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @size.deleter
    def size(self):
        del self.__size