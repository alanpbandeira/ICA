import struct, math
import numpy as np


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
            k += math.pow(2, x) * int(byte[::-1][x])
        byte_value_list.append(k)

    # Char value of each int
    #
    char_list = [chr(value) for value in byte_value_list]

    # Join the values to mount the packed value
    #
    joined = ''.join(char_list)

    # Convert the string of bytes to it`s float value
    #
    unpacked = struct.unpack('!f', joined)

    # Return the float value converted from bit_string
    #
    return unpacked[0]

print(bitStringToFloat('1'))