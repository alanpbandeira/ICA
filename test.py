import struct, math

def floatToBitString(num):
    # Struct can provide us with the float packed into bytes. The '!' ensures that
    # it's in network byte order (big-endian) and the 'f' says that it should be
    # packed as a float. Alternatively, for double-precision, you could use 'd'.
    packed = struct.pack('!f', num)

    # For each character in the returned string, we'll turn it into its corresponding
    # integer code point
    #
    # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
    integers = [c for c in packed]

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
    #unpacked = struct.unpack('!f', joined)

    # Return the float value converted from bit_string
    #
    #return unpacked[0]

print (bitStringToFloat(floatToBitString(1.0)))