"""
    Name: visuals.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import matplotlib.pyplot as plt


def plot_graph(x_values, y_values, title, x_label, y_label):

    plt.plot(x_values, y_values, color='green', linestyle=':')

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)

    plt.show()
