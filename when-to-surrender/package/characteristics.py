"""
    Name: characteristics.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.genotype import DIMENSION
from package.visuals import plot_graph
import math

GENERATIONS_IDX = 0
BEST_FIT_IDX = 1
EVALS_IDX = 2
GENERATION_ZERO = 1


def calc_expected_value(population):
    expected_values = []
    population_size = len(population.members)

    for _ in range(DIMENSION):
        expected_values.append(0)

    for i in range(population_size):
        for j in range(DIMENSION):
            expected_values[j] += population.members[i].chromosome[j]

    for i in range(DIMENSION):
        expected_values[i] /= population_size

    return expected_values


def calc_standard_deviation(population):
    standard_deviations = []
    expected_values = calc_expected_value(population)
    population_size = len(population.members)

    for i in range(DIMENSION):
        tmp_sum = 0
        for j in range(population_size):
            tmp_sum += math.pow(population.members[j].chromosome[i] - expected_values[i], 2)

        s_deviation = math.sqrt(tmp_sum / population_size)
        standard_deviations.append(s_deviation)

    return standard_deviations


def check_sd_criterion(population, epsilon):
    standard_deviations = calc_standard_deviation(population)

    for i in range(DIMENSION):
        if standard_deviations[i] > epsilon:
            return False

    return True


def check_k_iterations_criterion(k_best_fit, k_best_gen, k_value, population):
    if population.generation - k_best_gen >= k_value and k_best_fit < population.members[0].fitness:
        return True
    else:
        return False


def merge_data(runs):  # merge [[], [], ...] into []

    number_of_runs = len(runs)

    mean_generations = 0
    mean_best_fit = 0
    mean_evals = 0

    for i in range(number_of_runs):
        number_of_generations = len(runs[i].data[GENERATIONS_IDX])
        best_fit_in_run = runs[i].data[BEST_FIT_IDX][number_of_generations - 1]

        mean_generations += number_of_generations + GENERATION_ZERO
        mean_best_fit += best_fit_in_run
        mean_evals += runs[i].data[EVALS_IDX]

    mean_generations /= number_of_runs
    mean_best_fit /= number_of_runs
    mean_evals /= number_of_runs

    return [mean_generations, mean_best_fit, mean_evals]


class Data:

    def __init__(self, data):
        self.data = data
        self.x_label = 'Generation'
        self.y_label = 'min{Q(X)}'
        self.title = 'F4'

    def plot_graph(self):
        plot_graph(self.data[GENERATIONS_IDX], self.data[BEST_FIT_IDX], self.title, self.x_label, self.y_label)
