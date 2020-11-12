"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random


class Individual:
    fitness = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def rand_genome(cls, x_left_lim, x_right_lim, y_left_lim, y_right_lim):
        return cls(random.uniform(x_left_lim, x_right_lim), random.uniform(y_left_lim, y_right_lim))
