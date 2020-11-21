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

ITERATIONS = 2


def show_test_output(data):

    output_data = FunctionOptimizationData(data, ITERATIONS)
    output_data.print_sd_crit_stats()
    output_data.print_k_iter_crit_stats()


def run_tests():
    data = [[], [], []]

    f4 = optproblems.cec2005.F4(DIMENSION)  # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
    f5 = optproblems.cec2005.F5(DIMENSION)  # Schwefel’s Problem 2.6 with Global Optimum on Bounds
    f6 = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function

    print('Running F4...')
    print('\tRunning by standard deviation criterion...')
    data[F4].append(merge_data(MultipleRunsData(run_multiple_optimizations(f4, F4_BOUND,
                                                                           run_by_sd_criterion))))
    print('\tDone.')
    print('\tRunning by k-iterations criterion...')
    data[F4].append(merge_data(MultipleRunsData(run_multiple_optimizations(f4, F4_BOUND,
                                                                           run_by_k_iterations_criterion))))
    print('\tDone.')
    print('Done running F4')

    print('Running F5...')
    print('\tRunning by standard deviation criterion...')
    data[F5].append(merge_data(MultipleRunsData(run_multiple_optimizations(f5, F5_BOUND,
                                                                           run_by_sd_criterion))))
    print('\tDone.')
    print('\tRunning by k-iterations criterion...')
    data[F5].append(merge_data(MultipleRunsData(run_multiple_optimizations(f5, F5_BOUND,
                                                                           run_by_k_iterations_criterion))))
    print('\tDone.')
    print('Done running F5')

    # print('Running F6...')
    # runs.append(Data(run_cec(F6)))
    # print('Done running F6')

    print('### Done testing. ###')

    return data


def run_multiple_optimizations(cec_function, bounds, criterion):
    runs = []

    for _ in range(ITERATIONS):
        runs.append(optimize(cec_function, bounds, criterion))

    return runs
