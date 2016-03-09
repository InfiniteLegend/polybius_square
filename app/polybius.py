"""
Module which contains all necessary logic to use Polybius algorithm.

"""

import math

import numpy as np


def get_optimal_dimension(length):
    """
    Calculates best dimension for Polybius rectangle or square.

    :param length:
    :return:
    """

    sqrt = math.sqrt(length)

    # If length perfectly suits for square - return square root.
    if length % sqrt == 0:
        print "Square {0}x{0} found!".format(sqrt)
        return (sqrt, sqrt)

    # If doesn't - find best matching rectangle sizes.
    a = int(sqrt)
    while a > 1:
        b = length / a
        if isinstance(b, int):
            print "Rectangle {}x{} found!".format(a, b)
            return (a, b)
        a -= 1

    # Something can go wrong. Print error.
    # TODO: Write something better here.
    raise Exception()


def get_char_square():
    """
    Returns list of chars in a square/rectangle format.

    :return:
    """

    chars = [chr(i) for i in xrange(33, 124)] + [chr(i) for i in xrange(192, 256)]
    chars = np.array(chars)

    dimension = get_optimal_dimension(len(chars))


