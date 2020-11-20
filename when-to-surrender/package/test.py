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

from package.population import *
from package.characteristics import *
from package.visuals import *

DECIMAL_POINTS = 2
F4_BOUND = 100
EPSILON_DEVIATION = 40


def run_cec():
    f5 = optproblems.cec2005.F4(DIMENSION)  # Schwefel's Problem 2.6 with Global Optimum on Bounds
    return optimize(f5, F4_BOUND)


def optimize(function, bounds):
    population = Population.rand_population(MU, function, bounds)

    best_evals = []
    generations = []
    std_deviation = []

    for i in range(DIMENSION):
        std_deviation.append([])

    while population.generation != 100 and not(standard_deviation_criterion(population, EPSILON_DEVIATION)):
        print(population.generation)
        generations.append(population.generation)
        best_evals.append(population.members[0].fitness)

        tmp_sd = standard_deviation(population)
        for i in range(DIMENSION):
            std_deviation[i].append(tmp_sd[i])

        evolution(population, function, bounds)

        if standard_deviation_criterion(population, EPSILON_DEVIATION):
            break

    return [generations, best_evals]
