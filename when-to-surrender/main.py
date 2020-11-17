"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from population import *


MU = 20
LAMBDA = 5 * MU
F6_BOUND = 100


def evolution(population, function):
    selection = select(population, LAMBDA)
    offspring = mate(selection, function)
    population.members = mutate(population.members, function, F6_BOUND)
    offspring = mutate(offspring, function, F6_BOUND)
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
