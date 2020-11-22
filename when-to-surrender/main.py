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

ARGC = 4


def main():
    argv = sys.argv[1:]
    """
       0 - function to optimize
        1 - k value for k-iterations criterion 
        2 - epsilon for standard deviation criterion
        3 - epsilon for best-worst criterion
    """
    if len(argv) == ARGC:
        fun = argv[0]
        K_ITERATIONS = argv[1]
        EPSILON_DEVIATION = argv[2]
        EPSILON_BEST_WORST = argv[3]
        test_output = run_tests(fun)
        print('{} stats:'.format(fun))
        show_test_output(test_output)
    else:
        test_output = run_tests('F4')
        print('F4 stats:')
        show_test_output(test_output)

    # graph_data = optimize(optproblems.cec2005.F4(DIMENSION), F4_BOUND, tmp_criterion)
    # plot_graph(graph_data[0], graph_data[1], 'F4', 'Generation', 'minVal{F(X)}')


if __name__ == '__main__':
    main()
