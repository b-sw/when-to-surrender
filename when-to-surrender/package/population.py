"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from individual import Individual
from fitness import ackley_fitness
import random


def select(population, how_many):
    tmp_generation = []

    for _ in range(how_many):
        tmp_generation.append(random.choice(population.members))

    return tmp_generation


def mate(members, how_many):
    children = []
    # average with random weight
    for _ in range(how_many):
        child_genotype = []
        parent_1 = random.choice(members)
        parent_2 = random.choice(members)
        weight = random.uniform(0, 1)

        for i in range(len(parent_1.x)):
            child_genotype.append(weight * parent_1.x[i] + (1 - weight) * parent_2.x[i])

        child = Individual(child_genotype)
        child.fitness = ackley_fitness(child)
        children.append(child)

    return children


def mutate(population):
    return population


def succession(population, children, population_size):
    population.members.extend(children)
    population.members = sorted(population.members, key=lambda x: x.fitness)
    population.members = population.members[:population_size]


class Population:
    generation = 1

    def __init__(self, members):
        self.members = members

    @classmethod
    def rand_population(cls, size, x_left_lim, x_right_lim, y_left_lim, y_right_lim):
        members = []

        for _ in range(size):
            member = Individual.rand_genome(x_left_lim, x_right_lim, y_left_lim, y_right_lim)
            member.fitness = ackley_fitness(member)
            members.append(member)

        return cls(members)
