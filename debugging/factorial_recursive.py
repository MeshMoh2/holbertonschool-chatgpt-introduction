#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The number to compute the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert it to an integer, and compute its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
