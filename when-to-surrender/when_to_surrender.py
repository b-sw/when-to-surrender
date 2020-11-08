"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from .individual import Individual
from .population import Population
import random

POPULATION_SIZE = 100
PARENT_FIRST_PROB = 0.45
PARENT_SEC_PROB = 0.90
TARGET = 'How you doin'
FOUND = False


def rand_population(size):
    members = []

    for _ in range(size):
        rand_gnome = Individual.rand_gnome()
        individual = Individual(rand_gnome)
        individual.fitness = calc_fitness(individual)
        members.append(individual)

    population = Population(members)
    return population


def calc_fitness(member):
    global TARGET
    fitness = 0
    for curr, target in zip(member.chromosome, TARGET):
        if curr != target:
            fitness += 1
    return fitness


def mate(parent1, parent2):
    global PARENT_FIRST_PROB
    global PARENT_SEC_PROB

    child_chromosome = []
    for c_par1, c_par2 in zip(parent1.chromosome, parent2.chromosome):

        prob = random.random()

        if prob < PARENT_FIRST_PROB:
            child_chromosome.append(c_par1)

        elif prob < PARENT_SEC_PROB:
            child_chromosome.append(c_par2)

        else:
            child_chromosome.append(Individual.rand_gene())

    return Individual(child_chromosome)


def evolution(population):
    global FOUND
    population.members = sorted(population.members, key=lambda x: x.fitness)

    if population.members[0].fitness <= 0:
        FOUND = True
        return population

    new_generation = []

    # Elitism - 10% fittest survive
    survivors = int((10 * POPULATION_SIZE) / 100)
    new_generation.extend(population.members[:survivors])

    # Individuals from 50% of the fittest will mate and produce offspring
    survivors = int((90 * POPULATION_SIZE) / 100)
    for _ in range(survivors):
        parent1 = random.choice(population.members[:50])
        parent2 = random.choice(population.members[:50])
        child = mate(parent1, parent2)
        child.fitness = calc_fitness(child)
        new_generation.append(child)

    population.members = new_generation
    population.generation += 1

    print("Generation: {}\tString: {}\tFitness: {}"
          .format(population.generation,
                  "".join(population.members[0].chromosome),
                  population.members[0].fitness))


def run_evolution():
    global POPULATION_SIZE
    global FOUND

    population = rand_population(POPULATION_SIZE)

    while not FOUND:
        evolution(population)

    print("Generation: {}\tString: {}\tFitness: {}"
          .format(population.generation,
                  "".join(population.members[0].chromosome),
                  population.members[0].fitness))


run_evolution()
