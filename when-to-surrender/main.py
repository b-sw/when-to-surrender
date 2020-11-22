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
        argv[0] = function to optimize
        argv[1] = k value for k-iterations criterion / epsilon for standard deviation criterion
    """
    if len(argv) == ARGC:
        print(argv[0])
        print(argv[1])
        fun = argv[0]
        optimize.EPSILON_DEVIATION = argv[1]
        optimize.K_ITERATIONS = argv[1]
        optimize.EPSILON_BEST_WORST = argv[1]
        print(EPSILON_DEVIATION)
        print(K_ITERATIONS)
        print(EPSILON_BEST_WORST)
    else:
        test_output = run_tests('F4')
        print('F4 stats:')
        show_test_output(test_output)

    # graph_data = optimize(optproblems.cec2005.F4(DIMENSION), F4_BOUND, tmp_criterion)
    # plot_graph(graph_data[0], graph_data[1], 'F4', 'Generation', 'minVal{F(X)}')


if __name__ == '__main__':
    main()
