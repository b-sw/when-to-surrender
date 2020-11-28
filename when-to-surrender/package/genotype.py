"""
    Name: genotype.py
    Purpose: implementation of (mu + lambda) evolutionary strategy

    @author Bartosz Świtalski, Piotr Frątczak

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random
import math
import numpy


SIGMA_RANGE = 0.1
DIMENSION = 10
MEAN = 0
SIGMA = 1


def next_sigma(sigma, a):

    b = numpy.random.normal(MEAN, SIGMA)
    tau = 1 / math.sqrt(2 * DIMENSION)
    tau_prim = 1 / math.sqrt(2 * math.sqrt(DIMENSION))
    sigma_j = sigma * math.exp(tau_prim * a + tau * b)

    return sigma_j


class Genotype:

    def __init__(self, chromosome, fitness):
        self.chromosome = chromosome
        self.fitness = fitness

        self.sigma = [random.uniform(1 - SIGMA_RANGE, 1 + SIGMA_RANGE)]

        a = numpy.random.normal(MEAN, SIGMA)
        for i in range(1, DIMENSION):
            sigma_j = next_sigma(self.sigma[i-1], a)
            self.sigma.append(sigma_j)
