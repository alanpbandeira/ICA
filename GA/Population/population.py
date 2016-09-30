from ..IndividualModel.individual import Individual


class Population:

    __similarity = None
    __population_fitness = None

    def __init__(self, individual_list=None, size=100):
        """
        @Info: In case no individual_list is provided the population will be randomly created.
        @param
        @param
        @param
        """
        self.__size = size

        if individual_list:
            self.individual_list = individual_list
        else:
            self.individual_list = [Individual() for count in range(self.__size)]

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