# BMI 203 - HW 1

[![Build
Status](https://travis-ci.org/david-joy/bmi203-hw1.svg?branch=master)](https://travis-ci.org/david-joy/bmi203-hw1)

David Joy
1/24/2017

## Implement BubbleSort and Quicksort for integers

BubbleSort is implemented in [bubblesort()](https://github.com/david-joy/bmi203-hw1/blob/master/hw1/algs.py#L12)<br/>
<br/>
Quicksort is implemented in [quicksort()](https://github.com/david-joy/bmi203-hw1/blob/master/hw1/algs.py#L69), with auxilary functions [_quicksort()](https://github.com/david-joy/bmi203-hw1/blob/master/hw1/algs.py#L61) and [_quicksort_partition()](https://github.com/david-joy/bmi203-hw1/blob/master/hw1/algs.py#L36)

## Count the number of assignments

* BubbleSort:
    * `(n outer loops) * (n-1 + n-2 + ... 1 inner loops) * (2 assignments worst case)`
    * `n * (n - 1)/2 * 2 = n**2 + n`
    * `O(n**2)` assignments
* Quicksort:
    * `(2 * (r - p) assigns per partition worst case)`
    * p starts at 0, r at n - 1, so `2 * (r - p) = 2n - 2`
    * `O(n)` total assignments

## Count the number of conditionals

* BubbleSort:
    * `(n outer loops) * (n-1 + n-2 + ... 1 inner loops) * (2 compares)`
    * `n * (n - 1)/2 * 2 = n**2 + n`
    * `O(n**2)` conditionals
* Quicksort:
    * `(r - p compares per partition)`
    * p starts at 0, so `r - p = n`
    * Average case:
        * A random partition splits the array into roughly equal pieces. Assuming all partitions are roughly equal, we recurse `O(log(n))` times.
        * Total conditions `O(n*log(n))`
    * Worst case:
        * A bad partition splits the array into splits of size 1, n - 1. Since each split reduces the size of the array by 1, we recurse `n` times.
        * Total conditions `O(n**2)`

## Test some typical edge cases for sorting and run them on Travis

All tests are implemented in `test/test_algs.py`

Some cases to think of:

* Empty vector - [test_bubblesort_zero_elements()](https://github.com/david-joy/bmi203-hw1/blob/master/test/test_algs.py#L23)
* Single element vector - [test_bubblesort_one_element()](https://github.com/david-joy/bmi203-hw1/blob/master/test/test_algs.py#L32)
* Duplicated elements - [test_bubblesort_many_elements()](https://github.com/david-joy/bmi203-hw1/blob/master/test/test_algs.py#L61)
* Odd vs even length of input vector - [test_bubblesort_many_elements_even()](https://github.com/david-joy/bmi203-hw1/blob/master/test/test_algs.py#L71)

Tests for quicksort are also provided with the same naming convention.

## Test the time complexity of your algorithms as follows:

* For sizes of 100, 200, 300, ... 1000 
* Generate 100 random vectors 
* Sort them using your code

The sorting simulation is implemented in [plot_time_complexity.py](https://github.com/david-joy/bmi203-hw1/blob/master/plot_time_complexity.py)

The output plot is written to `images/time_complexity.png`

<img src="images/time_complexity.png">

Fitting `O(n**2)` and `O(n log(n))` to each data set, BubbleSort most closely fits `O(n**2)` while Quicksort most closely fits `O(n log(n))` on average.

## Installing

To use the package, first run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `hw1/__main__.py`) can be run as follows

```
python -m hw1
```

## Testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
