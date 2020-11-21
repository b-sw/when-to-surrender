"""
    Name: properties.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.genotype import DIMENSION
from package.visuals import plot_graph
import math

BEST_MEMBER = 0


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
    if population.generation - k_best_gen >= k_value and k_best_fit < population.members[BEST_MEMBER].fitness:
        return True
    else:
        return False
