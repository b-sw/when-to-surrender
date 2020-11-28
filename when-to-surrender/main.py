"""
    Name: script.py
    Purpose: execution interface

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.test import *
import getopt
import sys

ARGC = 7


def main():
    argv = sys.argv[1:]
    """
        0 - function to optimize
        1 - criterion
        2-5 - criterion parameters
        6 - graph destination file
    """

    if len(argv) == ARGC:
        fun = argv[0]
        criterion = argv[1]
        parameters = []
        for i in range(2, ARGC - 1):
            parameters.append(float(argv[i]))
        graph_filename = argv[6]
        test_output = run_tests(fun, criterion, parameters)
        show_test_output(test_output, criterion, parameters, graph_filename)
    else:
        test_output = run_tests('F5', 'sd', [0.05, 0.03, 0.015, 0.01])
        show_test_output(test_output, 'sd', [
                         0.05, 0.03, 0.015, 0.01], 'tmp_graph')


if __name__ == '__main__':
    main()
