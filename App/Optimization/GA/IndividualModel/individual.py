import struct, math
import numpy as np


class Individual:
    """
    @attribute: (PB), [np 1-Dm Array] - chromosome
    @attribute: (PV), [Numeric value] - fitness
    @attribute: (PV), [Numeric value] - prob_reproduction
    @attribute: (PV), [Numeric value]
    @attribute: (PB), [Integer value] - n_genes
    @attribute: (PB), [String value ] - individual_id

    """

    chromosome = []
    __fitness = None
    __rep_probability = None

    def __init__(self, rand=True, n_value=None, n_genes=32):
        """
        - Initialize the individual element.
        :param rand [default = True]: Set the init method to generate a random individual.
        :param n_value [default = None]: Represent the numeric value used to identify and build the individual.
        :param n_genes [default = 32]: Represent the size of the chromossome bit array.
        """
        self.n_genes = n_genes

        if rand:
            self.__chromosome = self.buildRandomIndividual()
            self.__n_value = self.bitStringToFloat(self.chromosomeToBitString())
            self.__individual_id = str(n_value)
        else:
            self.__chromosome = self.buildChromossome(n_value)
            self.__n_value = n_value
            self.__individual_id = str(n_value)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# CHROMOSSOME MANIPULATION METHODS
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def buildChromossome(self, value):
        """
        Sets the __chromossome as an bitArray of a numeric value
        :param value: numeric value to be converted in bitArray
        :return: None
        """

        return self.bitStringToChromossome(self.floatToBitString(value))

    def buildRandomIndividual(self, valued=None, num_range=None):
        """
        Creates a binary chromossome modeled as an array
        :return npArray:
        """
        if valued:
            num = np.random.uniform(num_range[0], num_range[1], 1)[0]
            return self.bitStringToChromossome(self.floatToBitString(num))
        else:
            return [1 if np.random.randint(1, 10, 1)[0] <= 5 else 0 for x in range(self.n_genes)]

    def chromosomeToBitString(self):
        """
        Convert a chromossome array to an analogue string.
        :return bit_string: A string of binary digits.
        """

        return ''.join([str(bit) for bit in self.__chromosome])

    def bitStringToChromossome(self, bit_string):
        """
        Convert a string of binary digits to a npArray.
        :param bit_string: A string of binary digits.
        :return npArray:  A numpy array of binary digits.
        :return String: String with error alert.
        """

        try:
            return [int(char) for char in bit_string]
        except IndexError:
            return 'Bit array too long, chromossome length is %d' % self.n_genes


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# NUMERIC VALUES MANIPULATION METHODS
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


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
                k += int(math.pow(2, x)) * int(byte[::-1][x])
            byte_value_list.append(k)

        # Char value of each int
        #
        char_list = [chr(value) for value in byte_value_list]
        
        # Join the values to mount the packed value
        #
        joined = bytearray(''.join(char_list), 'utf-8')
        print(joined)
        if len(joined) is 5:
            del joined[1]

        # Convert the string of bytes to it`s float value
        #
        unpacked = struct.unpack('!f', joined)

        # Return the float value converted from bit_string
        #
        return unpacked[0]


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# - PROPERTIES METHODS
#
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    @fitness.deleter
    def fitness(self):
        del self.__fitness

    @property
    def rep_probability(self):
        return self.__rep_probability

    @rep_probability.setter
    def rep_probability(self, value):
        self.rep_probability = value

    @rep_probability.deleter
    def rep_probability(self):
        del self.__rep_probability

    @property
    def n_value(self):
        return self.__n_value

    @n_value.setter
    def n_value(self, value):
        self.n_value = value

    @n_value.deleter
    def n_value(self):
        del self.n_value

    @property
    def individual_id(self):
        return self.__individual_id

    @individual_id.setter
    def individual_id(self, value):
        self.__individual_id = value

    @individual_id.deleter
    def individual_id(self):
        del self.__individual_id

