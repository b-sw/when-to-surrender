"""
    Name: script.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from package.test import *
import getopt
import sys

ITERATIONS = 5
ARGC = 2


def main():
    argv = sys.argv[1:]
    """
        argv[0] = epsilon for standard deviation criterion
        argv[1] = k value for k-iterations criterion
    """
    if len(argv) == ARGC:
        test.EPSILON_DEVIATION = argv[0]
        test.K_ITERATIONS = argv[1]

    runs = [[], []]

    print('Running by standard deviation criterion...')
    for i in range(ITERATIONS):
        # print('Run no {}\t Status: In progress'.format(i))
        runs[SD_CRIT].append(Data(run_cec(SD_CRIT)))
        # print('Run no {}\t Status: Done'.format(i))
    print('Done.')

    print('Running by k-iterations criterion...')
    for i in range(ITERATIONS):
        # print('Run no {}\t Status: In progress'.format(i))
        runs[K_ITER_CRIT].append(Data(run_cec(K_ITER_CRIT)))
        # print('Run no {}\t Status: Done'.format(i))
    print('Done.')

    # for i in range(ITERATIONS):
    #     runs[i].plot_graphs()

    mean_score_sd = merge_data(runs[SD_CRIT])
    mean_score_k_iter = merge_data(runs[K_ITER_CRIT])

    print("SD:\t\tNo runs: {}\t|\tGenerations mean: {}\t|\tBest fit mean: {}\t|\tNumber of evals mean: {}"
          .format(ITERATIONS,
                  round(mean_score_sd[GENERATIONS_IDX], DECIMAL_POINTS),
                  round(mean_score_sd[BEST_FIT_IDX], DECIMAL_POINTS),
                  round(mean_score_sd[EVALS_IDX], DECIMAL_POINTS)))

    print("K-iter\t\tNo runs: {}\t|\tGenerations mean: {}\t|\tBest fit mean: {}\t|\tNumber of evals mean: {}"
          .format(ITERATIONS,
                  round(mean_score_k_iter[GENERATIONS_IDX], DECIMAL_POINTS),
                  round(mean_score_k_iter[BEST_FIT_IDX], DECIMAL_POINTS),
                  round(mean_score_k_iter[EVALS_IDX], DECIMAL_POINTS)))


if __name__ == '__main__':
    main()
