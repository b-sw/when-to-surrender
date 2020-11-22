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
        1 - k value for k-iterations criterion 
        2 - epsilon for standard deviation criterion
        3 - epsilon for best-worst criterion
        4 - epsilon for variance criterion
    """
    global K_ITERATIONS
    global EPSILON_DEVIATION
    global EPSILON_BEST_WORST
    global EPSILON_VARIANCE

    if len(argv) == ARGC:
        fun = argv[0]
        K_ITERATIONS = argv[1]
        EPSILON_DEVIATION = argv[2]
        EPSILON_BEST_WORST = argv[3]
        EPSILON_VARIANCE = argv[4]
        test_output = run_tests(fun)
        print('{} Stats for K_VALUE: {} \t SD_EPSILON: {} \t BW_EPSILON: {} \t V_EPSILON: {}:'
              .format(fun, K_ITERATIONS, EPSILON_DEVIATION, EPSILON_BEST_WORST, EPSILON_VARIANCE))
        show_test_output(test_output)
    else:
        test_output = run_tests('F4')
        print('F4 stats for K_VALUE: {} \t SD_EPSILON: {} \t BW_EPSILON: {} \t V_EPSILON: {}:'
              .format(K_ITERATIONS, EPSILON_DEVIATION, EPSILON_BEST_WORST, EPSILON_VARIANCE))
        show_test_output(test_output)


if __name__ == '__main__':
    main()
