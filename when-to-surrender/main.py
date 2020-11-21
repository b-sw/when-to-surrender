"""
    Name: script.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.test import *
import getopt
import sys

ARGC = 2


def main():
    argv = sys.argv[1:]
    """
        argv[0] = epsilon for standard deviation criterion
        argv[1] = k value for k-iterations criterion
    """
    if len(argv) == ARGC:
        test.EPSILON_DEVIATION = argv[0]
        test.K_ITERATIONS = argv[1]

    test_output = run_tests()
    show_test_output(test_output[F4])
    show_test_output(test_output[F5])


if __name__ == '__main__':
    main()
