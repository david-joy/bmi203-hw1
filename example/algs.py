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


def _quicksort_partition(x, p, r):
    # Work out where we should split the array to partition it
    pivot_item = x[p]
    left = p
    right = r
    keepgoing = True
    while keepgoing:
        # Move left while item less than pivot
        while left <= right and x[left] <= pivot_item:
            left += 1
        # Move right while item greater than pivot
        while right >= left and x[right] > pivot_item:
            right -= 1
        if left < right:
            # swap left and right
            x[left], x[right] = x[right], x[left]
        else:
            # Pointers crossed, we're done
            keepgoing = False
    # Right is the final position for the pivot
    x[p] = x[right]
    x[right] = pivot_item
    return right


def _quicksort(x, p, r):
    # Implement the inplace quicksort function
    if r > p:
        pivot = _quicksort_partition(x, p, r)
        _quicksort(x, p, pivot - 1)
        _quicksort(x, pivot + 1, r)


def quicksort(x):
    """ This function is a wrapper that sets up the recursion

    It then calls _quicksort with the appropriate arguments
    """
    n = x.shape[0]
    # Any list with fewer than 2 element is sorted
    if n < 2:
        return x.copy()
    x = x.copy()  # Make a copy of x we can mess with
    _quicksort(x, 0, n - 1)  # Do an inplace sort
    return x  # Return the sorted copy
