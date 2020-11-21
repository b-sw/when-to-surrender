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
F5_BOUND = 100
F6_BOUND = 100
EPSILON_DEVIATION = 0.7
K_ITERATIONS = 10
BUDGET = 10000 * DIMENSION

SD_CRIT = 0
K_ITER_CRIT = 1

# F4 = 0
# F5 = 0
# F6 = 0


def show_test_output():
    pass


def run_tests():
    pass


def run_cec(which):

    # cec_data = []

    f4 = optproblems.cec2005.F4(DIMENSION)  # Shifted Schwefel’s Problem 1.2 with Noise in Fitness
    # f5 = optproblems.cec2005.F5(DIMENSION)  # Schwefel’s Problem 2.6 with Global Optimum on Bounds
    # f6 = optproblems.cec2005.F6(DIMENSION)  # Shifted Rosenbrock’s Function

    if which == SD_CRIT:
        return optimize(f4, F4_BOUND, run_by_sd_criterion)
    elif which == K_ITER_CRIT:
        return optimize(f4, F4_BOUND, run_by_k_iterations_criterion)


def optimize(function, bounds, criterion):
    population = Population.rand_population(MU, function, bounds)

    generations = []
    best_evals = []
    number_of_evals = MU  # MU is the number of P0 evals

    [generations, best_evals, number_of_evals] = criterion(function, bounds, population, generations,
                                                           best_evals, number_of_evals)

    # print('Best eval: {}\t|\tNumber of generations: {}'.format(population.members[0].fitness, population.generation))

    return [generations, best_evals, number_of_evals]


def run_by_sd_criterion(function, bounds, population, generations,
                        best_evals, number_of_evals):
    while (number_of_evals + MU + LAMBDA) < BUDGET \
            and not (check_sd_criterion(population, EPSILON_DEVIATION)):
        generations.append(population.generation)
        best_evals.append(population.members[0].fitness)

        evolution(population, function, bounds)

        number_of_evals += (MU + LAMBDA)

    return [generations, best_evals, number_of_evals]


def run_by_k_iterations_criterion(function, bounds, population, generations,
                                  best_evals, number_of_evals):
    k_best_fit = population.members[0].fitness
    k_best_gen = population.generation

    while (number_of_evals + MU + LAMBDA) < BUDGET \
            and not(check_k_iterations_criterion(k_best_fit, k_best_gen, K_ITERATIONS, population)):
        generations.append(population.generation)
        best_evals.append(population.members[0].fitness)

        evolution(population, function, bounds)

        number_of_evals += (MU + LAMBDA)

        if population.members[0].fitness < k_best_fit:
            k_best_fit = population.members[0].fitness
            k_best_gen = population.generation

    return [generations, best_evals, number_of_evals]
