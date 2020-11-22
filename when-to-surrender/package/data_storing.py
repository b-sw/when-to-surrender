"""
    Name: properties.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.visuals import *

DECIMAL_POINTS = 2

GENERATIONS_IDX = 0
BEST_FITS_IDX = 1
EVALS_IDX = 2
GENERATION_ZERO_SHIFT = 1

K_ITER_DATA_IDX = 0
SD_DATA_IDX = 1
BEST_WORST_DATA_IDX = 2
VARIANCE_DATA_IDX = 3


def merge_data(multiple_runs):  # merge [[run1_data], [run2_data], ...] into [mean_run_data]

    number_of_runs = len(multiple_runs.runs_data)

    mean_generations = 0
    mean_best_fit = 0
    mean_evals = 0

    for i in range(number_of_runs):
        number_of_generations = len(multiple_runs.runs_data[i][GENERATIONS_IDX])
        best_fit_in_run = multiple_runs.runs_data[i][BEST_FITS_IDX][number_of_generations - GENERATION_ZERO_SHIFT]

        mean_generations += number_of_generations + GENERATION_ZERO_SHIFT
        mean_best_fit += best_fit_in_run
        mean_evals += multiple_runs.runs_data[i][EVALS_IDX]

    mean_generations /= number_of_runs
    mean_best_fit /= number_of_runs
    mean_evals /= number_of_runs

    return [mean_generations, mean_best_fit, mean_evals]


class MultipleRunsData:

    def __init__(self, runs_data):
        self.runs_data = runs_data
        self.x_label = 'Generation'
        self.y_label = 'min{Q(X)}'
        self.title = 'F4'


class FunctionOptimizationData:

    def __init__(self, data, iterations, params, criterion_name):
        self.crit_data = data
        self.iterations = iterations
        self.params = params
        self.number_of_params = len(params)
        self.criterion_name = criterion_name

    def print_stats(self):
        for i in range(self.number_of_params):
            print("{} |\t\tNo runs: {}\t|\tGenerations mean: {}\t\t|"
                  "\tBest fit mean: {}\t\t|\tNumber of evals mean: {}"
                  .format(self.criterion_name, self.iterations,
                          round(self.crit_data[i][GENERATIONS_IDX], DECIMAL_POINTS),
                          round(self.crit_data[i][BEST_FITS_IDX], DECIMAL_POINTS),
                          round(self.crit_data[i][EVALS_IDX], DECIMAL_POINTS)))

        self.plot_best_fits_graph()

    def plot_best_fits_graph(self):
        fits_values = []
        for i in range(self.number_of_params):
            fits_values.append(round(self.crit_data[i][BEST_FITS_IDX]))
        plot_graph(self.params, fits_values, self.criterion_name, 'Params', 'Best fit mean')

    def plot_evals_graph(self):
        pass
