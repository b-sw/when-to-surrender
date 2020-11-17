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

DECIMAL_POINTS = 2


def optimize(function, bounds):
    population = Population.rand_population(MU, function, bounds)

    while population.generation != 100:
        evolution(population, function, bounds)

        print("Generation: {}\tBest fit: {}"
              .format(population.generation, round(population.members[0].fitness, DECIMAL_POINTS)))
