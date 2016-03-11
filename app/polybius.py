"""
Module which contains all necessary logic to use Polybius algorithm.

"""

import math

import numpy as np


def uniqify(password):
    """
    Method that uniqifies password (deletes repeated symbols) and returns password
    as list.

    :param password:
    :return:
    """

    password = list(password)

    seen = {}
    result = []

    for char in password:
        if char in seen: continue
        seen[char] = 1
        result.append(char)

    return result


def get_char_square(password=None):
    """
    Returns list of chars in a square/rectangle format.

    :param password:
    :return:
    """

    chars = list()
    condition = lambda i: True

    if password:
        chars += uniqify(password)
        condition = lambda i: not chr(i) in password

    chars += [chr(i) for i in xrange(44, 124) if condition(i)] + [chr(i) for i in xrange(192, 256) if condition(i)]
    chars = np.array(chars)

    dimension = math.sqrt(len(chars))

    chars = np.reshape(chars, (dimension, ) * 2)

    return chars
