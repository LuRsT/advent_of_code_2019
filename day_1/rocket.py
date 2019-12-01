import math


def round_down(n, decimals=0):
    """
    Rouding down in python is odd:
        https://realpython.com/python-rounding/
    """
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def calculate_fuel(mass):
    return round_down(mass / 3) - 2


if __name__ == "__main__":
    with open("input", "r") as input_file:
        requirements = []
        for line in input_file.readlines():
            requirements.append(calculate_fuel(int(line)))
        print(sum(requirements))
