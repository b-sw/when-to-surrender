"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""

from population import *

POPULATION_SIZE = 50
ACKLEY_LEFT_LIM = -5
ACKLEY_RIGHT_LIM = 5


def evolution(population):
    children = mate(select(population, POPULATION_SIZE * 7), POPULATION_SIZE * 7)
    # todo: mutate
    succession(population, children, POPULATION_SIZE)
    population.generation += 1


def main():
    population = Population.rand_population(POPULATION_SIZE, ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM,
                                            ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM)

    while population.generation != 100:
        evolution(population)
        print("Generation: {}\tX: {}\tY: {}\tFitness: {}"
              .format(population.generation,
                      population.members[0].x[0],
                      population.members[0].x[1],
                      population.members[0].fitness))
        if population.members[0].fitness == 0:
            break


if __name__ == '__main__':
    main()
