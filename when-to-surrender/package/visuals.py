"""
    Name: visuals.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import matplotlib.pyplot as plt


def plot_graph(x_values, y_values, title, x_label, y_label):

    plt.bar(x_values, y_values, color=['cornflowerblue', 'orange', 'purple', 'limegreen'], linestyle=':')

    plt.xticks(x_values, x_values)
    plt.yticks(y_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)

    plt.savefig("graphs/" + title + ".pdf")

    # plt.show()
