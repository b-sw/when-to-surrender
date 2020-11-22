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

ARGC = 6


def main():
    argv = sys.argv[1:]
    """
        0 - function to optimize
        1 - criterion
        2-5 - criterion parameters
    """

    if len(argv) == ARGC:
        fun = argv[0]
        criterion = argv[1]
        for i in range(ARGC - 2):
            parameters.append(float(argv[i]))
        test_output = run_tests(fun, criterion, parameters)
        print('{} stats for {} parameter = {}'
              .format(fun, criterion, parameters))
        show_test_output(test_output, params, criterion)
    else:
        test_output = run_tests('F4', 'k-iter', [1, 2, 3, 4])
        print('F4 stats for {} parameters: {}'
              .format('k-iter', [1, 2, 3, 4]))
        show_test_output(test_output, 'k-iter', [1, 2, 3, 4])


if __name__ == '__main__':
    main()
