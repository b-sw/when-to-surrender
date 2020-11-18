"""
    Name: characteristics.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.genotype import DIMENSION
import math


def expected_value(population):

    expected_values = []
    population_size = len(population.members)

    for _ in range(DIMENSION):
        expected_values.append(0)

    for i in range(population_size):
        for j in range(DIMENSION):
            expected_values[j] += population.members[i].chromosome[j]

    for i in range(DIMENSION):
        expected_values[i] /= DIMENSION

    return expected_values


def standard_deviation(population):

    standard_deviations = []
    expected_values = expected_value(population)
    population_size = len(population.members)

    for i in range(DIMENSION):
        tmp_sum = 0
        for j in range(population_size):
            tmp_sum += math.pow(population.members[j].chromosome[i] - expected_values[i], 2)

        s_deviation = math.sqrt(tmp_sum / population_size)
        standard_deviations.append(s_deviation)

    return standard_deviations
