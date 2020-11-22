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

    if len(argv) == ARGC:
        fun = argv[0]
        k_iterations = argv[1]
        epsilon_deviation = argv[2]
        epsilon_best_worst = argv[3]
        epsilon_variance = argv[4]
        set_parameters(k_iterations, epsilon_deviation, epsilon_best_worst, epsilon_variance)
        test_output = run_tests(fun)
        print('{} Stats for K_VALUE: {} \t SD_EPSILON: {} \t BW_EPSILON: {} \t V_EPSILON: {}:'
              .format(fun, k_iterations, epsilon_deviation, epsilon_best_worst, epsilon_variance))
        show_test_output(test_output)
    else:
        k_iterations = 5
        epsilon_deviation = 10
        epsilon_best_worst = 10000
        epsilon_variance = 1000000
        set_parameters(k_iterations, epsilon_deviation, epsilon_best_worst, epsilon_variance)
        test_output = run_tests('F4')
        print('F4 stats for K_VALUE: {} \t SD_EPSILON: {} \t BW_EPSILON: {} \t V_EPSILON: {}:'
              .format(k_iterations, epsilon_deviation, epsilon_best_worst, epsilon_variance))
        show_test_output(test_output)


if __name__ == '__main__':
    main()
