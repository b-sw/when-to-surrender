"""
    Name: test.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005
import os

from package.optimize import *
from package.data_storing import *

F4 = 0
F5 = 1
F6 = 2
F4_BOUND = 100
F5_BOUND = 100
F6_BOUND = 100

ITERATIONS = 10


def show_test_output(data):
    output_data = FunctionOptimizationData(data, ITERATIONS)
    output_data.print_k_iter_crit_stats()
    output_data.print_sd_crit_stats()
    output_data.print_best_worst_crit_stats()
    output_data.print_variance_crit_stats()


def run_tests(function):
    data = []

    if function == 'F4':
        f = optproblems.cec2005.F4(DIMENSION)  # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
        bound = F4_BOUND
    elif function == 'F5':
        f = optproblems.cec2005.F5(DIMENSION)  # Schwefel’s Problem 2.6 with Global Optimum on Bounds
        bound = F5_BOUND
    elif function == 'F6':
        f = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function
        bound = F6_BOUND

    print('Running {}...'.format(function))
    # print('\tRunning by k-iterations criterion...')
    data.append(merge_data(MultipleRunsData(run_multiple_optimizations(f, bound,
                                                                       run_by_k_iterations_criterion))))
    # print('\tDone.')
    # print('\tRunning by standard deviation criterion...')
    data.append(merge_data(MultipleRunsData(run_multiple_optimizations(f, bound,
                                                                       run_by_sd_criterion))))
    # print('\tDone.')
    # print('\tRunning by best-worst criterion...')
    data.append(merge_data(MultipleRunsData(run_multiple_optimizations(f, bound,
                                                                       run_by_best_worst_criterion))))
    # print('\tRunning by variance criterion...')
    data.append(merge_data(MultipleRunsData(run_multiple_optimizations(f, bound,
                                                                       run_by_variance_criterion))))
    # print('\tDone.')

    print('### Done testing. ###')

    return data


def run_multiple_optimizations(cec_function, bounds, criterion):
    runs = []

    for _ in range(ITERATIONS):
        runs.append(optimize(cec_function, bounds, criterion))

    return runs
