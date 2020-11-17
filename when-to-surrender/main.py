"""
    Name: main.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from package.test import *

F6_BOUND = 100
F9_BOUND = 5
F12_BOUND = math.pi


def main():
    f6 = optproblems.cec2005.F6(DIMENSION)
    f9 = optproblems.cec2005.F9(DIMENSION)
    f12 = optproblems.cec2005.F12(DIMENSION)

    # optimize(f6, F6_BOUND)
    optimize(f9, F9_BOUND)
    # optimize(f12, F12_BOUND)


if __name__ == '__main__':
    main()
