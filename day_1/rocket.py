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


def calculate_fuel_v2(mass):
    fuel = calculate_fuel(mass)
    next_ = calculate_fuel(fuel)
    if next_ < 0:
        return fuel
    else:
        total = fuel + next_
        while next_ > 0:
            next_ = calculate_fuel(next_)
            if next_ > 0:
                total += next_
        return total


def get_result_from_input_file(callable):
    with open("input", "r") as input_file:
        requirements = []
        for line in input_file.readlines():
            requirements.append(callable(int(line)))
        return sum(requirements)


if __name__ == "__main__":
    print(get_result_from_input_file(calculate_fuel))
    print(get_result_from_input_file(calculate_fuel_v2))
