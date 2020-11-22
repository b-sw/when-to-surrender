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
K_ITERATIONS = 1
EPSILON_DEVIATION = 1
EPSILON_BEST_WORST = 1
EPSILON_VARIANCE = 1


def set_parameters(k_iterations, epsilon_deviation, epsilon_best_worst, epsilon_variance):
    global K_ITERATIONS
    global EPSILON_DEVIATION
    global EPSILON_BEST_WORST
    global EPSILON_VARIANCE

    K_ITERATIONS = k_iterations
    EPSILON_DEVIATION = epsilon_deviation
    EPSILON_BEST_WORST = epsilon_best_worst
    EPSILON_VARIANCE = epsilon_variance


def optimize(function, bounds, criterion):
    population = Population.rand_population(MU, function, bounds)

    generations = []
    best_evals = []
    number_of_evals = MU  # MU is the number of P0 evals

    [generations, best_evals, number_of_evals] = criterion(function, bounds, population, generations,
                                                           best_evals, number_of_evals)

    # print('Best eval: {}\t|\tNumber of generations: {}'.format(population.members[0].fitness, population.generation))

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
