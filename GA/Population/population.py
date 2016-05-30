from ..IndividualModel.individual import Individual

class Population:
    def __init__(self, size=100, max_size=None):
        self.__size = size
        self.__max_size = max_size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @size.deleter
    def size(self):