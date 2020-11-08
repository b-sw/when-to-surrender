"""
    Name:
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import random

GNOME_LEN = 12
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''


class Individual:

    fitness = 0

    def __init__(self, chromosome):
        self.chromosome = chromosome

    @classmethod
    def rand_gene(cls):
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def rand_gnome(cls):
        return [cls.rand_gene() for _ in range(GNOME_LEN)]