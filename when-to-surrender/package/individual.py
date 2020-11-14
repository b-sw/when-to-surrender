"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random


class Individual:
    fitness = 0                 # the bigger the better

    def __init__(self, x):
        self.x = x

    @classmethod
    def rand_genome(cls, x_left_lim, x_right_lim, y_left_lim, y_right_lim):
        x = [random.uniform(x_left_lim, x_right_lim), random.uniform(y_left_lim, y_right_lim)]
        return cls(x)
