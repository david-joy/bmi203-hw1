#!/usr/bin/env python3

""" Script to test the time complexity """

# Imports

# Standard lib
import pathlib
import time

# 3rd party
import numpy as np

import matplotlib.pyplot as plt

# Our own imports
from hw1 import algs

# Range of sizes to test
ARRAY_SIZES = np.arange(100, 1100, 100)

# Number of random vectors to generate
NUM_VECTORS = 100


def time_sorting(sort_fxn, data):
    """ Record the run times for each run of a sorting function

    :param sort_fxn:
        The sort function of form sort_fxn(vec) to call
    :param data:
        A list of vectors to sort
    :returns:
        A list of run times to sort each element in data
    """
    times = [time.process_time()]
    for vec in data:
        sort_fxn(vec)
        times.append(time.process_time())
    return [t1 - t0 for t0, t1 in zip(times[:-1], times[1:])]


def fit_data(xdata, ydata, mode='linear'):
    """ Fit the data """

    xorig = xdata.copy()

    # Fix x and y to be the same shape
    xdata = xdata[:, np.newaxis]
    xdata = np.repeat(xdata, ydata.shape[1], axis=1)

    assert xdata.shape == ydata.shape

    xdata = xdata.flatten()
    ydata = ydata.flatten()

    if mode == 'linear':
        A = np.array([np.ones_like(xdata), xdata])
    elif mode == 'quadratic':
        A = np.array([np.ones_like(xdata), xdata**2])
    elif mode == 'loglinear':
        A = np.array([np.ones_like(xdata), xdata * np.log(xdata)])
    else:
        raise KeyError('Unknown mode "{}"'.format(mode))

    coeffs = np.linalg.lstsq(A.T, ydata)[0]

    if mode == 'linear':
        yfull = xdata * coeffs[1] + coeffs[0]
        yorig = xorig * coeffs[1] + coeffs[0]
    elif mode == 'quadratic':
        yfull = xdata**2 * coeffs[1] + coeffs[0]
        yorig = xorig**2 * coeffs[1] + coeffs[0]
    elif mode == 'loglinear':
        yfull = xdata * np.log(xdata) * coeffs[1] + coeffs[0]
        yorig = xorig * np.log(xorig) * coeffs[1] + coeffs[0]
    res = np.sqrt(np.sum((yfull - ydata)**2))
    return yorig, res


def main():

    bubblesort_times = []
    quicksort_times = []

    # Try sorting data for each size
    for size in ARRAY_SIZES:
        print('Sorting arrays of size {}'.format(size))

        # Generate data
        data = [np.random.randint(-50, 51, size=(size, ))
                for _ in range(NUM_VECTORS)]

        # Time bubblesort
        bubblesort_time = time_sorting(algs.bubblesort, data)
        print('Bubblesort {} took {:1.1f} secs'.format(size, np.sum(bubblesort_time)))
        bubblesort_times.append(bubblesort_time)

        # Time quicksort
        quicksort_time = time_sorting(algs.quicksort, data)
        print('Quicksort {} took {:1.1f} secs'.format(size, np.sum(quicksort_time)))
        quicksort_times.append(quicksort_time)

    bubblesort_times = np.array(bubblesort_times)
    quicksort_times = np.array(quicksort_times)

    # Do linear, n log n, quadratic fits
    bubblesort_quadratic = fit_data(ARRAY_SIZES, bubblesort_times, mode='quadratic')
    bubblesort_loglinear = fit_data(ARRAY_SIZES, bubblesort_times, mode='loglinear')
    bubblesort_q_res = bubblesort_quadratic[1]
    bubblesort_l_res = bubblesort_loglinear[1]

    quicksort_quadratic = fit_data(ARRAY_SIZES, quicksort_times, mode='quadratic')
    quicksort_loglinear = fit_data(ARRAY_SIZES, quicksort_times, mode='loglinear')
    quicksort_q_res = quicksort_quadratic[1]
    quicksort_l_res = quicksort_loglinear[1]

    # And make plots

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    ax0, ax1 = axes

    ax0.plot(ARRAY_SIZES, bubblesort_times, 'ob')
    ax0.plot(ARRAY_SIZES, bubblesort_quadratic[0], '-r',
             linewidth=3, label='$O(n^2)$ R = %1.1e' % bubblesort_q_res)
    ax0.plot(ARRAY_SIZES, bubblesort_loglinear[0], '-g',
             linewidth=3, label='$O(n*log(n))$ R = %1.1e' % bubblesort_l_res)
    ax0.legend(loc='upper left')

    ax0.set_xlabel('Size of array (elements)')
    ax0.set_ylabel('Time to sort array (seconds)')
    ax0.set_title('BubbleSort Time Complexity')

    ax1.plot(ARRAY_SIZES, quicksort_times, 'ob')
    ax1.plot(ARRAY_SIZES, quicksort_quadratic[0], '-r',
             linewidth=3, label='$O(n^2)$ R = %1.1e' % quicksort_q_res)
    ax1.plot(ARRAY_SIZES, quicksort_loglinear[0], '-g',
             linewidth=3, label='$O(n*log(n))$ R = %1.1e' % quicksort_l_res)
    ax1.legend(loc='upper left')

    ax1.set_xlabel('Size of array (elements)')
    ax1.set_ylabel('Time to sort array (seconds)')
    ax1.set_title('Quicksort Time Complexity')

    outdir = pathlib.Path('images')
    outdir.mkdir(parents=True, exist_ok=True)

    outfile = outdir / 'time_complexity.png'
    print('Saving output in {}'.format(outfile))

    fig.savefig(str(outfile))
    plt.close()


if __name__ == '__main__':
    main()
