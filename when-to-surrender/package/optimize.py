"""
    Name: optimize.py
    Purpose: termination criteria execution

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.population import *
from package.properties import *

BUDGET = 10000 * DIMENSION
K_ITERATIONS = 0
EPSILON_DEVIATION = 0
EPSILON_BEST_WORST = 0
EPSILON_VARIANCE = 0
OPTIMUM_BIAS = 0


def set_parameters(which, value, bias):
    global K_ITERATIONS
    global EPSILON_DEVIATION
    global EPSILON_BEST_WORST
    global EPSILON_VARIANCE
    global OPTIMUM_BIAS

    if which == 'k-iter':
        K_ITERATIONS = value
    elif which == 'sd':
        EPSILON_DEVIATION = value
    elif which == 'best-worst':
        EPSILON_BEST_WORST = value
    elif which == 'variance':
        EPSILON_VARIANCE = value

    OPTIMUM_BIAS = bias


def optimize(function, bounds, criterion):
    population = Population.rand_population(MU, function, bounds)

    best_evals = []
    number_of_evals = MU  # MU is the number of P0 evals

    [best_evals, number_of_evals] = criterion(function, bounds, population,
                                              best_evals, number_of_evals)

    return [best_evals, number_of_evals]


def run_by_k_iterations_criterion(function, bounds, population, best_evals, number_of_evals):
    k_best_fit = population.members[BEST_MEMBER].fitness
    k_best_gen = population.generation

    while number_of_evals + LAMBDA < BUDGET \
            and not (check_k_iterations_criterion(k_best_fit, k_best_gen, K_ITERATIONS, population)):

        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds, OPTIMUM_BIAS)

        number_of_evals += LAMBDA

        if population.members[BEST_MEMBER].fitness < k_best_fit:
            k_best_fit = population.members[BEST_MEMBER].fitness
            k_best_gen = population.generation

    return [best_evals, number_of_evals]


def run_by_sd_criterion(function, bounds, population, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_sd_criterion(population, EPSILON_DEVIATION)):
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds, OPTIMUM_BIAS)

        number_of_evals += LAMBDA

    return [best_evals, number_of_evals]


def run_by_best_worst_criterion(function, bounds, population, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_best_worst_criterion(population, EPSILON_BEST_WORST)):
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds, OPTIMUM_BIAS)

        number_of_evals += LAMBDA

    return [best_evals, number_of_evals]


def run_by_variance_criterion(function, bounds, population, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_variance_criterion(population, EPSILON_VARIANCE)):
        best_evals.append(population.members[BEST_MEMBER].fitness)
        evolution(population, function, bounds, OPTIMUM_BIAS)

        number_of_evals += LAMBDA

    return [best_evals, number_of_evals]
