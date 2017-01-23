import numpy as np


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1, 2, 3])


def bubblesort(x):
    """ Sort by looping through x and swapping pairs if p0 > p1

    Repeat this n times, causing the smallest elements to bubble to the top
    """
    n = x.shape[0]
    # Any list with fewer than 2 element is sorted
    if n < 2:
        return x

    # Loop through every element of the array
    for i in range(n):
        # With each loop, smaller elements step bubble up one step
        # This means the last element is sorted in the first pass
        # Second last in the second pass
        # etc...
        for j in range(1, n - i):
            # Compare and swap, works for any objects that define __gt__
            p0, p1 = x[j - 1], x[j]
            if p0 > p1:
                x[j - 1], x[j] = p1, p0
    return x


def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    return
