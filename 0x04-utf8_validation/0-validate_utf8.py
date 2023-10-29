#!/usr/bin/python3
"""Method to validate UTF-8 encoding"""

def validUTF8(data):
    """Function to check if a byte is a valid UTF-8"""
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]

        """Check the number of bytes in the current character"""
        if (byte & 0b10000000) == 0:
            i += 1
        elif (byte & 0b11100000) == 0b11000000:
            if i + 1 < len(data) and is_continuation(data[i + 1]):
                i += 2
            else:
                return False
        elif (byte & 0b11110000) == 0b11100000:
            if (
                i + 2 < len(data)
                and is_continuation(data[i + 1])
                and is_continuation(data[i + 2])
            ):
                i += 3
            else:
                return False
        elif (byte & 0b11111000) == 0b11110000:
            if (
                i + 3 < len(data)
                and is_continuation(data[i + 1])
                and is_continuation(data[i + 2])
                and is_continuation(data[i + 3])
            ):
                i += 4
            else:
                return False

    return True

