"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""

from population import *

MU = 50
LAMBDA = 5 * MU

POPULATION_SIZE = MU
ACKLEY_LEFT_LIM = -5
ACKLEY_RIGHT_LIM = 5


def evolution(population):
    selection = select(population, LAMBDA)
    offspring = mate(selection)
    # todo: mutate
    # todo: fitness(offspring)
    population.members = succession(population, offspring, MU)
    population.generation += 1


def main():
    population = Population.rand_population(POPULATION_SIZE, ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM,
                                            ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM)
    # todo: fitness(population)
    while population.generation != 100:
        evolution(population)
        print("Generation: {}\tX: {}\tY: {}\tFitness: {}"
              .format(population.generation,
                      population.members[0].x[0],
                      population.members[0].x[1],
                      population.members[0].fitness))
        # todo: find a surrender strategy
        if population.members[0].fitness == 0:
            break


if __name__ == '__main__':
    main()
