"""
    Name: test.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from package.optimize import *
from package.data_storing import *

F4_BOUND = 100
F5_BOUND = 100
F6_BOUND = 100
F4_OPT_BIAS = -450
F5_OPT_BIAS = -310
F6_OPT_BIAS = 390

ITERATIONS = 25
PARAMS = 4


def show_test_output(data, criterion_name, params):
    output_data = FunctionOptimizationData(data, ITERATIONS, params, criterion_name)
    output_data.print_stats()


def run_tests(function, criterion_name, parameters):

    data = []

    if function == 'F4':
        f = optproblems.cec2005.F4(DIMENSION)  # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
        bound = F4_BOUND
        bias = F4_OPT_BIAS
    elif function == 'F5':
        f = optproblems.cec2005.F5(DIMENSION)  # Schwefel’s Problem 2.6 with Global Optimum on Bounds
        bound = F5_BOUND
        bias = F5_OPT_BIAS
    else:  # if function == 'F6':
        f = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function
        bound = F6_BOUND
        bias = F6_OPT_BIAS

    # print('Running {} by {} - No runs: {}...'.format(function, criterion_name, ITERATIONS))

    if criterion_name == 'k-iter':
        criterion = run_by_k_iterations_criterion
    elif criterion_name == 'sd':
        criterion = run_by_sd_criterion
    elif criterion_name == 'best-worst':
        criterion = run_by_best_worst_criterion
    else:  # if criterion_name == 'variance':
        criterion = run_by_variance_criterion

    for i in range(PARAMS):
        set_parameters(criterion_name, parameters[i], bias)
        data.append(merge_data(run_multiple_optimizations(f, bound, criterion)))

    return data


def run_multiple_optimizations(cec_function, bounds, criterion):
    runs = []

    for _ in range(ITERATIONS):
        runs.append(optimize(cec_function, bounds, criterion))

    return runs
