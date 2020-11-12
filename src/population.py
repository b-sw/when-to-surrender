"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from individual import Individual


class Population:
    generation = 1

    def __init__(self, members):
        self.members = members

    @classmethod
    def rand_population(cls, size, x_left_lim, x_right_lim, y_left_lim, y_right_lim):
        members = []

        for _ in range(size):
            member = Individual.rand_genome(x_left_lim, x_right_lim, y_left_lim, y_right_lim)
            members.append(member)

        return cls(members)
