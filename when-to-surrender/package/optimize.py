"""
    Name: optimize.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.population import *
from package.properties import *

BUDGET = 10000 * DIMENSION
K_ITERATIONS = 5
EPSILON_DEVIATION = 10
EPSILON_BEST_WORST = 10000
EPSILON_VARIANCE = 1000000


def set_parameters(which, value):
    global K_ITERATIONS
    global EPSILON_DEVIATION
    global EPSILON_BEST_WORST
    global EPSILON_VARIANCE

    if which == 'k-iter':
        K_ITERATIONS = value
    elif which == 'sd':
        EPSILON_DEVIATION = value
    elif which == 'best-worst':
        EPSILON_BEST_WORST = value
    elif which == 'variance':
        EPSILON_VARIANCE = value


def optimize(function, bounds, criterion):
    population = Population.rand_population(MU, function, bounds)

    generations = []
    best_evals = []
    number_of_evals = MU  # MU is the number of P0 evals

    [generations, best_evals, number_of_evals] = criterion(function, bounds, population, generations,
                                                           best_evals, number_of_evals)

    return [generations, best_evals, number_of_evals]  # later just return criterion(...)


def run_by_k_iterations_criterion(function, bounds, population, generations, best_evals, number_of_evals):
    k_best_fit = population.members[BEST_MEMBER].fitness
    k_best_gen = population.generation

    while number_of_evals + LAMBDA < BUDGET \
            and not (check_k_iterations_criterion(k_best_fit, k_best_gen, K_ITERATIONS, population)):

        generations.append(population.generation)
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds)

        number_of_evals += LAMBDA

        if population.members[BEST_MEMBER].fitness < k_best_fit:
            k_best_fit = population.members[BEST_MEMBER].fitness
            k_best_gen = population.generation

    return [generations, best_evals, number_of_evals]


def run_by_sd_criterion(function, bounds, population, generations, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_sd_criterion(population, EPSILON_DEVIATION)):

        generations.append(population.generation)
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds)

        number_of_evals += LAMBDA

    return [generations, best_evals, number_of_evals]


def run_by_best_worst_criterion(function, bounds, population, generations, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_best_worst_criterion(population, EPSILON_BEST_WORST)):

        generations.append(population.generation)
        best_evals.append(population.members[BEST_MEMBER].fitness)

        evolution(population, function, bounds)

        number_of_evals += LAMBDA

    return [generations, best_evals, number_of_evals]


def run_by_variance_criterion(function, bounds, population, generations, best_evals, number_of_evals):
    while number_of_evals + LAMBDA < BUDGET \
            and not (check_variance_criterion(population, EPSILON_VARIANCE)):
        generations.append(population.generation)
        best_evals.append(population.members[BEST_MEMBER].fitness)
        evolution(population, function, bounds)

        number_of_evals += LAMBDA

    return [generations, best_evals, number_of_evals]
