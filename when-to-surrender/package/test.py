"""
    Name: test.py
    Purpose: benchmark interface

    @author Bartosz Świtalski, Piotr Frątczak

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

ITERATIONS = 51
PARAMS = 4

DATA_IDX = 0
BOXPLOT_DATA_IDX = 1
FUNCTION_IDX = 2


def show_test_output(data, criterion_name, params, graph_filename):
    output_data = FunctionOptimizationData(
        data[DATA_IDX], ITERATIONS, params, criterion_name)
    plot_boxplot(data[BOXPLOT_DATA_IDX], params, graph_filename)
    output_data.print_stats()


def run_tests(function, criterion_name, parameters):

    data = []
    boxplot_data = []

    if function == 'F4':
        # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
        f = optproblems.cec2005.F4(DIMENSION)
        bound = F4_BOUND
        bias = F4_OPT_BIAS
    elif function == 'F5':
        # Schwefel’s Problem 2.6 with Global Optimum on Bounds
        f = optproblems.cec2005.F5(DIMENSION)
        bound = F5_BOUND
        bias = F5_OPT_BIAS
    else:  # if function == 'F6':
        f = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function
        bound = F6_BOUND
        bias = F6_OPT_BIAS

    print('Running {} by {} - No runs: {}...'.format(function,
                                                     criterion_name, ITERATIONS))

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
        runs = run_multiple_optimizations(f, bound, criterion)

        data.append(merge_data(runs))
        boxplot_data.append(boxplot_from_multiple_runs(runs))

    return [data, boxplot_data]


def run_multiple_optimizations(cec_function, bounds, criterion):
    runs = []

    for i in range(ITERATIONS):
        runs.append(optimize(cec_function, bounds, criterion))

    return runs
