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

ARGC = 5


def main():
    argv = sys.argv[1:]
    """
        0 - function to optimize
        1 - criterion
        2 - criterion parameter
    """

    if len(argv) == ARGC:
        fun = argv[0]
        criterion = argv[1]
        parameter = float(argv[2])
        test_output = run_tests(fun, criterion, parameter)
        print('{} stats for {} parameter = {}'
              .format(fun, criterion, parameter))
        show_test_output(test_output)
    else:
        test_output = run_tests('F4', 'variance', 1)
        print('F4 stats for {} parameter: {}'
              .format('k-iter', K_ITERATIONS))
        show_test_output(test_output)


if __name__ == '__main__':
    main()
