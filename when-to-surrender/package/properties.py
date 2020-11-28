"""
    Name: properties.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.genotype import *
from package.visuals import plot_graph
import math

BEST_MEMBER = 0


def calc_population_ev(population):
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


def calc_population_sd(population):
    standard_deviations = []
    expected_values = calc_population_ev(population)
    population_size = len(population.members)

    for i in range(DIMENSION):
        tmp_sum = 0
        for j in range(population_size):
            tmp_sum += math.pow(population.members[j].chromosome[i] - expected_values[i], 2)

        s_deviation = math.sqrt(tmp_sum / population_size)
        standard_deviations.append(s_deviation)

    return standard_deviations


def calc_fit_ev(population):
    expected_value = 0
    population_size = len(population.members)

    for i in range(population_size):
        expected_value += population.members[i].fitness

    expected_value /= population_size

    return expected_value


def calc_list_sd(values, expected):
    length = len(values)
    tmp_sum = 0
    for i in range(length):
        tmp_sum += math.pow(values[i] - expected, 2)

    standard_deviation = math.sqrt(tmp_sum / length)

    return standard_deviation


def calc_variance(population):
    fitness_variance = 0
    expected_fit = calc_fit_ev(population)
    population_size = len(population.members)

    tmp_sum = 0
    for i in range(population_size):
        tmp_sum += math.pow(population.members[i].fitness - expected_fit, 2)

    fitness_variance = 1 / population_size * tmp_sum

    return fitness_variance


def check_k_iterations_criterion(k_best_fit, k_best_gen, k_value, population):
    if population.generation - k_best_gen >= k_value and k_best_fit <= population.members[BEST_MEMBER].fitness:
        return True
    else:
        return False


def check_sd_criterion(population, epsilon):
    standard_deviations = calc_population_sd(population)

    for i in range(DIMENSION):
        if standard_deviations[i] > epsilon:
            return False

    return True


def check_best_worst_criterion(population, epsilon):
    worst_member_idx = len(population.members) - 1
    best_fit = population.members[BEST_MEMBER].fitness
    worst_fit = population.members[worst_member_idx].fitness

    if math.fabs(best_fit - worst_fit) <= epsilon:
        return True
    else:
        return False


def check_variance_criterion(population, epsilon):
    fitness_variance = calc_variance(population)
    if fitness_variance <= epsilon:
        return True
    else:
        return False
