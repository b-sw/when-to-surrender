"""
    Name: script.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.test import *

ITERATIONS = 3


def main():
    runs = []

    for _ in range(ITERATIONS):
        runs.append(Data(run_cec()))

    # for i in range(ITERATIONS):
    #     runs[i].plot_graphs()

    mean_score = merge_data(runs)

    print("No runs: {}\t|\tGenerations mean: {}\t|\tBest fit mean: {}"
          .format(ITERATIONS,
                  round(mean_score[GENERATIONS_IDX], DECIMAL_POINTS),
                  round(mean_score[BEST_FIT_IDX], DECIMAL_POINTS)))


if __name__ == '__main__':
    main()
