#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the given number of rows.

    Parameters:
    - n: The number of rows in the Pascal's triangle.

    Returns:
    - result: A list of lists representing the Pascal's triangle.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    result = []  # Stores the rows of the Pascal's triangle
    prev = []  # Stores the previous row

    if n <= 0:
        return []  # Return an empty list if n is not a positive integer

    for i in range(n):
        if i == 0:
            # First row of the triangle, which only contains 1
            result.append([1])
            continue
        elif i == 1:
            # Second row of the triangle, which contains two 1's
            result.append([1, 1])
            prev = [1, 1]
            continue

        current = []  # Stores the current row being generated
        for j in range(len(prev)):
            if j == 0:
                current.append(1)  # First element of the row is always 1
                continue
            current.append(prev[j] + prev[j-1])
        current.append(1)  # Last element of the row is always 1
        result.append(current)  # Add the current row to the result list
        prev = current.copy()  # Update the previous row for the next iteration

    return result
