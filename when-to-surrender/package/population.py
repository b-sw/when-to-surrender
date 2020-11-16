"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random
import optproblems
import optproblems.cec2005

from genotype import *


def select(population, how_many):
    tmp_generation = []

    for _ in range(how_many):
        tmp_generation.append(random.choice(population.members))

    return tmp_generation


def mate(members, function):
    children_genotypes = []
    # average with random weight
    for _ in members:
        child_chromosome = []
        parent_1 = random.choice(members)
        parent_2 = random.choice(members)
        weight = random.uniform(0, 1)

        for i in range(DIMENSION):
            child_chromosome.append(weight * parent_1.chromosome[i] + (1 - weight) * parent_2.chromosome[i])

        child = optproblems.base.Individual(child_chromosome)
        function.evaluate(child)
        child_genotype = Genotype(child_chromosome, child.objective_values)
        children_genotypes.append(child_genotype)

    return children_genotypes


def mutate(population):
    pass


def succession(population, children, population_size):
    next_generation = population.members + children
    next_generation = sorted(next_generation, key=lambda x: x.fitness)
    return next_generation[:population_size]


class Population:
    generation = 1

    def __init__(self, members):
        self.members = members

    @classmethod
    def rand_population(cls, size, function, bound):        # single bound because most functions in the benchmark
        members = []                                        # have bounds of additive inverses [-x,x]

        for j in range(size):
            x = []
            for i in range(DIMENSION):
                x.append(random.uniform(-bound, bound))

            individual = optproblems.base.Individual(x)
            function.evaluate(individual)
            fitness = individual.objective_values
            #print("Individual {}\t Fitness: {}\tX: {}"
            #      .format(j, fitness, x))
            genotype = Genotype(x, fitness)
            members.append(genotype)

        return cls(members)
