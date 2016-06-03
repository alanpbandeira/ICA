import random
import struct
import numpy as np


class Individual:
    """
    @attribute: (PV), [np 1-Dm Array] - chromossome
    @attribute: (PV), [Numeric value] - fitness
    @attribute: (PV), [Numeric value] - prob_reproduction
    @attribute: (PB), [Integer value] - n_genes
    @attribute: (PB), [String value ] - individual_id

    """

    __chromosome = np.array([])
    __fitness = None
    __prob_reproduction = None

    def __init__(self, n_genes=32, rand=False, numeric=False, value=None, individual_id=None):
        self.n_genes = n_genes
        self.individual_id = individual_id

        if numeric:
            if rand:
                self.setRandomIndividual()
            else:
                self.setChromossome(value)

    def setRandomIndividual(self):
        for x in range(self.n_genes):
            coin = random.randint(1, 10)

            if coin <= 5:
                np.append(self.__chromosome, 1)
            else:
                np.append(self.__chromosome, 0)

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    @fitness.deleter
    def fitness(self):
        del self.__fitness

    def setChromossome(self, value):
        """
        Sets the __chromossome as an bitArray of a numeric value
        :param value: numeric value to be converted in bitArray
        :return: None
        """

        self.__chromosome = self.bitStringToChromossome(self.floatToBitString(value))

    def chromosomeToBitString(self):
        bit_string = ''
        for bit in self.__chromosome:
            bit_string += str(bit)

        return bit_string

    def integerToBitArray(self, value):
        temp_string = bin(value)[2:]
        self.n_genes = len(temp_string)
        return np.array([int(bit) for bit in temp_string])

    def bitStringToChromossome(self, bit_string):
        if len(bit_string) <= self.n_genes:
            return np.array([int(char) for char in bit_string])
        else:
            print('Bit array too long, chromossome length is %d' % self.n_genes)

    @staticmethod
    def floatToBitString(num):
        # Struct can provide us with the float packed into bytes. The '!' ensures that
        # it's in network byte order (big-endian) and the 'f' says that it should be
        # packed as a float. Alternatively, for double-precision, you could use 'd'.
        packed = struct.pack('!f', num)

        # For each character in the returned string, we'll turn it into its corresponding
        # integer code point
        #
        # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
        integers = [ord(c) for c in packed]

        # For each integer, we'll convert it to its binary representation.
        binaries = [bin(i) for i in integers]

        # Now strip off the '0b' from each of these
        stripped_binaries = [s.replace('0b', '') for s in binaries]

        # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
        #
        # ['00111110', '10100011', '11010111', '00001010']
        padded = [s.rjust(8, '0') for s in stripped_binaries]

        # At this point, we have each of the bytes for the network byte ordered float
        # in an array as binary strings. Now we just concatenate them to get the total
        # representation of the float:
        return ''.join(padded)

    @staticmethod
    def bitStringToFloat(bit_string):
        # Creates a network ordered byte list to be translated individually.
        #
        # ['00111110', '10100011', '11010111', '00001010']
        byte_string_list = []
        for start, end in zip([0, 8, 16, 24], [8, 16, 24, 32]):
            byte_string_list.append(bit_string[start:end])

        # Unpad the extra the 8-complement bits of each byte_string
        #
        # ['111110', '10100011', '11010111', '1010']
        unpadded = []
        for byte in byte_string_list:
            if byte.find('1') >= 0:
                unpadded.append(byte.lstrip('0'))
            else:
                unpadded.append('0')

        # Converts each bitstring to it's integer value
        #
        # [62, 163, 215, 10]
        byte_value_list = []
        for byte in byte_string_list:
            k = 0
            for x in range(len(byte)):
                k += np.power(2, x) * int(byte[::-1][x])
            byte_value_list.append(k)

        # Char value of each int
        char_list = [chr(value) for value in byte_value_list]

        # Join the values to mount the packed value
        #
        joined = ''.join(char_list)

        # Convert the string of bytes to it`s float value
        #
        unpacked = struct.unpack('!f', joined)
        return unpacked[0]

