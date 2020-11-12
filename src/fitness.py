"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import math


def ackley_fitness(member):
    return 1 / (-20 * math.exp(-0.2 * math.sqrt(1/2 * (member.x**2 + member.y**2)))
                - math.exp(1/2 * (math.cos(2 * math.pi * member.x) + math.cos(2 * math.pi * member.y)))
                + math.e + 20)
