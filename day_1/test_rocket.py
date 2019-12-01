# --- Day 1: The Tyranny of the Rocket Equation ---
#
# The Elves quickly load you into a spacecraft and prepare to launch.# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.
#
# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
#
# For example:
#
#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.

from rocket import calculate_fuel


def test_twelve():
    mass = 12

    result = calculate_fuel(mass)

    assert result == 2


def test_fourteen():
    mass = 14

    result = calculate_fuel(mass)

    assert result == 2


def test_thousand_nine_hundred_sixty_nine():
    mass = 1969

    result = calculate_fuel(mass)

    assert result == 654


def test_100756():
    mass = 100756

    result = calculate_fuel(mass)

    assert result == 33583
