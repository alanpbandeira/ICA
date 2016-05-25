import random
import struct
import numpy as np


class Individual:
    """

    """

    __chromosome = np.array([])
    __fitness = None
    __reproduction_probability = None

    def __init__(self, n_genes=4, rand=False, score=None):
        self.n_genes = n_genes
        self.score = score

        if rand:
            self.setRandomIndividual()

    def setRandomIndividual(self):
        for x in range(self.n_genes):
            coin = random.randint(1, 10)

            if coin <= 5:
                np.append(self.__chromosome, 1)
            else:
                np.append(self.__chromosome, 0)

    @staticmethod
    def convertNumToBitArray(value):
        bit_string = bin(value)[2:]

        bit_array = np.array([int(bit) for bit in bit_string])

        return bit_array

    def setSVChromossome(self, value):
        """
        Sets the __chromossome as an bitArray of a numeric value
        :param value: numeric value to be converted in bitArray
        :return: None
        """

        self.__chromosome = self.convertNumToBitArray(value)

    def setFitness(self, value):
        self.__fitness = value

    def getFitness(self):
        return self.__fitness

    def binary(num):
        # Struct can provide us with the float packed into bytes. The '!' ensures that
        # it's in network byte order (big-endian) and the 'f' says that it should be
        # packed as a float. Alternatively, for double-precision, you could use 'd'.
        packed = struct.pack('!f', num)
        print 'Packed: %s' % repr(packed)

        # For each character in the returned string, we'll turn it into its corresponding
        # integer code point
        #
        # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
        integers = [ord(c) for c in packed]
        print 'Integers: %s' % integers

        # For each integer, we'll convert it to its binary representation.
        binaries = [bin(i) for i in integers]
        print 'Binaries: %s' % binaries

        # Now strip off the '0b' from each of these
        stripped_binaries = [s.replace('0b', '') for s in binaries]
        print 'Stripped: %s' % stripped_binaries

        # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
        #
        # ['00111110', '10100011', '11010111', '00001010']
        padded = [s.rjust(8, '0') for s in stripped_binaries]
        print 'Padded: %s' % padded

        # At this point, we have each of the bytes for the network byte ordered float
        # in an array as binary strings. Now we just concatenate them to get the total
        # representation of the float:
        return ''.join(padded)


i = Individual()

print (i.convertNumToBitArray(2.5))