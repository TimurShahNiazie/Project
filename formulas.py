import math
import sys

def add(values) -> int:
    """
    using a list, it adds the first and second user input
    :param values: the first and second input
    :return: the sum of the first and second input
    """
    i = 0
    sum = 0
    while i < len(values):
            sum += values[i]
            i += 1
    return sum

def subtract(values) -> int:
    """
    subtracts the first and second input, reads using a list
    :param values: first and second input
    :return: the difference of first and second inpit
    """
    i = 0
    sum = 0
    check = 0
    sum = values[0] - values[1]
    return sum

def multiply(values) -> int:
    """
    using a list, it multiplies the first and second input
    while also checking for zeros
    :param values: first and second input
    :return: the product of the first and second input
    """
    i = 0

    sum = 1


    while i < len(values):
            sum *= values[i]
            i += 1
    return sum



def divide(values) -> float:
    """
    using a list to check for zeros, it divides the
    first and second input
    :param values: first and second input
    :return: the quotient of the first and second input
    """
    sum = values.pop(0)
    for val in values:
        if val == 0:
            raise ZeroDivisionError
        sum /= val
    return sum

