"""
    Name: main.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import optproblems
import optproblems.cec2005

from package.test import *
from package.visuals import *

F4_BOUND = 100


def main():

    f4 = optproblems.cec2005.F4(DIMENSION)

    data = optimize(f4, F4_BOUND)
    plot_graph(data[0], data[1], 'Best fit', 'generation', 'minVal')
    plot_graph(data[0], data[2][0], 'Standard deviation', 'generation', 'sigma(x0)')


if __name__ == '__main__':
    main()
