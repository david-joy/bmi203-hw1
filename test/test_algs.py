import numpy as np

from example import algs


def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    res = algs.pointless_sort(x)
    exp = np.array([1, 2, 3])
    assert np.array_equal(res, exp)

    # generate a new random vector of length 10
    x = np.random.rand(10)

    res = algs.pointless_sort(x)
    exp = np.array([1, 2, 3])
    assert np.array_equal(res, exp)


def test_bubblesort_zero_elements():
    x = np.array([])

    res = algs.bubblesort(x)
    exp = np.array([])

    assert np.array_equal(res, exp)


def test_bubblesort_one_element():
    x = np.array([7])

    res = algs.bubblesort(x)
    exp = np.array([7])

    assert np.array_equal(res, exp)


def test_bubblesort_two_elements_ordered():

    x = np.array([2, 7])

    res = algs.bubblesort(x)
    exp = np.array([2, 7])

    assert np.array_equal(res, exp)


def test_bubblesort_two_elements_disordered():

    x = np.array([5, -3])

    res = algs.bubblesort(x)
    exp = np.array([-3, 5])

    assert np.array_equal(res, exp)


def test_bubblesort_many_elements():

    x = np.array([1, 2, 4, 0, 1])

    res = algs.bubblesort(x)
    exp = np.array([0, 1, 1, 2, 4])

    assert np.array_equal(res, exp)


def test_bubblesort_many_elements_ordered():

    x = np.array([0, 1, 1, 2, 4])

    res = algs.bubblesort(x)
    exp = np.array([0, 1, 1, 2, 4])

    assert np.array_equal(res, exp)


def test_bubblesort_many_chr_elements():

    x = np.array(['a', 'c', 'b', 'a', 'b'])

    res = algs.bubblesort(x)
    exp = np.array(['a', 'a', 'b', 'b', 'c'])

    assert np.array_equal(res, exp)


def test_bubblesort_random_array():

    # generate random vector of length 100
    x = np.random.rand(100)

    res = algs.bubblesort(x)

    # Verify invariant
    assert np.all(res[1:] >= res[:-1])

    # compare to reference implementation
    exp = np.sort(x)

    assert np.array_equal(res, exp)


def test_quicksort_zero_elements():
    x = np.array([])

    res = algs.quicksort(x)
    exp = np.array([])

    assert np.array_equal(res, exp)


def test_quicksort_one_element():
    x = np.array([7])

    res = algs.quicksort(x)
    exp = np.array([7])

    assert np.array_equal(res, exp)


def test_quicksort_two_elements_ordered():

    x = np.array([2, 7])

    res = algs.quicksort(x)
    exp = np.array([2, 7])

    assert np.array_equal(res, exp)


def test_quicksort_two_elements_disordered():

    x = np.array([5, -3])

    res = algs.quicksort(x)
    exp = np.array([-3, 5])

    assert np.array_equal(res, exp)


def test_quicksort_many_elements():

    x = np.array([1, 2, 4, 0, 1])

    res = algs.quicksort(x)
    exp = np.array([0, 1, 1, 2, 4])

    assert np.array_equal(res, exp)


def test_quicksort_many_elements_ordered():

    x = np.array([0, 1, 1, 2, 4])

    res = algs.quicksort(x)
    exp = np.array([0, 1, 1, 2, 4])

    assert np.array_equal(res, exp)


def test_quicksort_many_chr_elements():

    x = np.array(['a', 'c', 'b', 'a', 'b'])

    res = algs.quicksort(x)
    exp = np.array(['a', 'a', 'b', 'b', 'c'])

    assert np.array_equal(res, exp)


def test_quicksort_random_array():

    # generate random vector of length 100
    x = np.random.rand(100)

    res = algs.quicksort(x)

    # Verify invariant
    assert np.all(res[1:] >= res[:-1])

    # compare to reference implementation
    exp = np.sort(x)

    assert np.array_equal(res, exp)
