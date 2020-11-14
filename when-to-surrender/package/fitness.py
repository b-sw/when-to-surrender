"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import math


def ackley_fitness(member):
    x = member.x[0]
    y = member.x[1]
    return (-20 * math.exp(-0.2 * math.sqrt(1/2 * (x**2 + y**2)))
                - math.exp(1/2 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
                + math.e + 20)
