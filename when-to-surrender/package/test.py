"""
    Name: test.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from package.population import *
from package.characteristics import *

DECIMAL_POINTS = 2


def optimize(function, bounds):

    population = Population.rand_population(MU, function, bounds)

    best_evals = []
    generations = []
    sd = []

    for i in range(DIMENSION):
        sd.append([])

    while population.generation != 100:
        generations.append(population.generation)
        best_evals.append(population.members[0].fitness)

        tmp_sd = standard_deviation(population)
        for i in range(DIMENSION):
            sd[i].append(tmp_sd[i])

        evolution(population, function, bounds)

        print("Generation: {}\tBest fit: {}"
              .format(population.generation, round(population.members[0].fitness, DECIMAL_POINTS)))

    return [generations, best_evals, sd]
