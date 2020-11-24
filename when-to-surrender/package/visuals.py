"""
    Name: visuals.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import matplotlib.pyplot as plt

BEST_EVALS_IDX = 0


def boxplot_from_multiple_runs(runs):
    data = []

    for i in range(len(runs)):
        number_of_generations = len(runs[i][BEST_EVALS_IDX])
        data.append(runs[i][BEST_EVALS_IDX][number_of_generations - 1])  # add best fit from run to data

    return data


def plot_boxplot(data, params):
    fig, ax = plt.subplots()

    ax.set_title('Best fits in 25 runs')
    ax.boxplot(data, labels=params)

    plt.show()


def plot_graph(x_values, y_values, title, x_label, y_label):
    plt.bar(x_values, y_values, color=['cornflowerblue', 'orange', 'purple', 'limegreen'], linestyle=':')

    plt.xticks(x_values, x_values)
    plt.yticks(y_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)
    plt.xlabel('Parameter')
    plt.ylabel('Best evals')

    plt.savefig("graphs/" + title + ".pdf")

    # plt.show()
