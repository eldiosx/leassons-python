"""
This is an example of a Python program that complies with PEP 8 style conventions.
"""

import math


def calculate_square_root(number):
    """
    This function calculates the square root of a number and rounds it to two decimal places.
    """
    result = math.sqrt(number)
    rounded_result = round(result, 2)
    return rounded_result


if __name__ == "__main__":
    # Example of using the calculate_root_square function
    NUMBER = 16
    square_root = calculate_square_root(NUMBER)
    print(f"The square root of {NUMBER} is {square_root}")
