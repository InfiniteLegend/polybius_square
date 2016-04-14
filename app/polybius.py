# -*- coding: utf-8 -*-
"""
Module which contains all necessary logic to use Polybius algorithm.

"""

import math
import sys
import locale
import json

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
        condition = lambda i: not unichr(i) in password

    chars += [unichr(i) for i in xrange(32, 127) if condition(i)]
    chars += [unichr(i) for i in xrange(1040, 1112) if condition(i)]
    chars += [unichr(i) for i in (1030, 1031)]
    chars = np.array(chars)

    dimension = math.sqrt(len(chars))

    chars = np.reshape(chars, (dimension, ) * 2)

    return chars


def encode(text, password=None):
    """
    Encoding message using polybius algorithm.

    :param text:
    :param password:
    :return:
    """
    chars = get_char_square(password)

    # Getting coordinates for each character.
    locations = [[location[0][0], location[1][0]] for location in [np.where(chars == char) for char in text]]

    # Listing them inline and grouping to pairs.
    locations = [location[0] for location in locations] + [location[1] for location in locations]
    locations = [[locations[i], locations[i+1]] for i in xrange(0, len(locations), 2)]

    text = u"".join([chars[location[0], location[1]] for location in locations])

    return json.dumps({
        "result": text
    })


def decode(text, password=None):
    """
    Decoding message using polybius algorithm.

    :param text:
    :param password:
    :return:
    """
    chars = get_char_square(password)

    # Getting coordinates for each character.
    locations = [[location[0][0], location[1][0]] for location in [np.where(chars == char) for char in text]]

    # Writing them inline iterating columns.
    new_locations = []
    for location in locations:
        new_locations += location

    # Devide them into two columns by center and immediately add character.
    center = int(len(new_locations) / 2)
    text = u"".join([chars[new_locations[i], new_locations[i + center]] for i in xrange(0, center)])

    return json.dumps({
        "result": text
    })

if __name__ == "__main__":
    text = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))

    decode(text)