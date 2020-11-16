"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from genotype import *
from population import *

MU = 20
LAMBDA = 5 * MU
F6_BOUND = 100


def evolution(population, function):
    selection = select(population, LAMBDA)
    offspring = mate(selection, function)
    # todo: mutate
    population.members = succession(population, offspring, MU)
    population.generation += 1


def main():
    f6 = optproblems.cec2005.F6(DIMENSION)
    population = Population.rand_population(MU, f6, F6_BOUND)

    while population.generation != 100:
        evolution(population, f6)

        print("Generation: {}\tBest individual's fitness: {}"
              .format(population.generation, population.members[0].fitness))


if __name__ == '__main__':
    main()
