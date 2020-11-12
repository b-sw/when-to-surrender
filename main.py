"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from src.population import Population
import fitness as fit

POPULATION_SIZE = 100
ACKLEY_LEFT_LIM = -5
ACKLEY_RIGHT_LIM = 5


def mate(parent1, parent2):
    pass


def evolution(population):
    population.generation += 1
    pass


def main():
    population = Population.rand_population(POPULATION_SIZE, ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM,
                                            ACKLEY_LEFT_LIM, ACKLEY_RIGHT_LIM)

    while population.generation != 100:
        evolution(population)
        print("Generation: {}\tX: {}\tY: {}\tFitness: {}"
              .format(population.generation,
                      population.members[0].x,
                      population.members[0].y,
                      population.members[0].fitness))


if __name__ == '__main__':
    main()
