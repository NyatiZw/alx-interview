#!/usr/bin/python3
"""
Method to calculate the fewest number of operations

Args:
    n: integer

Returns:
    integer value || 0
"""

import math


def minOperations(n):
    """
    Calculate the fewest number of operations to achive a goal.

    Args:
    n (int): The target integer.

    Returns:
    int: The fewest number of operations.
    """
    if not isinstance(n, int) or n <=0:
        return 0

    operations = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        operations += 1

    return operations
