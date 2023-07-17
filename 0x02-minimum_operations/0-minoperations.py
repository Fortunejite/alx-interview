#!/usr/bin/python3
"""Solves the minimum operation puzzle """


def minOperations(n):
    """Calculates the minimum number of operations to reach n characters
    Args:
        n (int): Number of characters to reach
    Returns:
        int: Minimum number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                operations += i
                n = n // i
                break

    return operations