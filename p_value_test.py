from LDP_Algorithms import GRR
from LDP_Algorithms import RR
from tqdm import tqdm
import numpy as np
import hypergeom as hypergeom
import matplotlib.pyplot as plt


def pValueTestNonVectorized(algo, epsilon, n=1000):
    D = algo.getD()
    p_values = []
    results = []
    for v1 in D:
        for v2 in D:
            if v1 < v2:
                O1 = []
                O2 = []
                for i in range(n):
                    O1.append(algo.f(v1))
                    O2.append(algo.f(v2))
                c1 = 0
                c2 = 0
                for v in D:
                    for el in O1:
                        if el == v:
                            c1 += 1
                    for el in O2:
                        if el == v:
                            c2 += 1
                    if c1 > c2:
                        p_val = pvalue(c1, c2, epsilon, n)
                    else:
                        p_val = pvalue(c2, c1, epsilon, n)
                    p_values.append(p_val)
                    results.append([epsilon, p_val, v1, v2,  n, v])
    return results

# ***** statdp github repo ***** #


def pvalue(cx, cy, epsilon, iterations):
    """ Calculate p-value based on observed results.
    :param cx: The observed count of running algorithm with database 1 that falls into the event
    :param cy:The observed count of running algorithm with database 2 that falls into the event
    :param epsilon: The epsilon to test for.
    :param iterations: The total iterations for running algorithm.
    :return: p-value
    """
    # average p value
    sample_num = 200
    p_value = 0
    for new_cx in np.random.binomial(cx, 1.0 / (np.exp(epsilon)), sample_num):
        p_value += hypergeom.sf(new_cx - 1, 2 * iterations,
                                iterations, new_cx + cy)
    return p_value / sample_num


def plot_result(data, xlabel, ylabel, output_filename):
    """plot the results similar to the figures in our paper
    :param data: The input data sets to plots. e.g., {algorithm_epsilon: [(test_epsilon, pvalue), ...]}
    :param xlabel: The label for x axis.
    :param ylabel: The label for y axis.
    :param title: The title of the figure.
    :param output_filename: The output file name.
    :return: None
    """
    # setup the figure
    plt.ylim(0.0, 1.0)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Results")

    # colors and markers for each claimed epsilon
    markers = ['s', 'o', '^', 'x', '*', '+', 'p']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    # add an auxiliary line for p-value=0.05
    plt.axhline(y=0.05, color='black', linestyle='dashed', linewidth=1.2)
    for i, (epsilon, points) in enumerate(data.items()):
        # add an auxiliary vertical line for the claimed privacy
        plt.axvline(x=float(epsilon), color=colors[i % len(
            colors)], linestyle='dashed', linewidth=1.2)
        # plot the
        x = [item[0] for item in points]
        p = [item[1] for item in points]
        plt.plot(x, p, 'o-',
                 label=f'$\\epsilon_0$ = {epsilon}', markersize=8, marker=markers[i % len(markers)], linewidth=3)

    # plot legends
    legend = plt.legend()
    legend.get_frame().set_linewidth(0.0)

    # save the figure and clear the canvas for next draw
    plt.savefig(output_filename, bbox_inches='tight')
    plt.gcf().clear()

# ***** statdp github repo ***** #


epsilon_results = {}
for epsilon in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
    grr = GRR.GRR(epsilon, 10)
    result = pValueTestNonVectorized(grr, epsilon, 10000)
    epsilon_results[epsilon] = result
    plot_result(epsilon_results, "epsilon",
                "p_value", "grr.png")
