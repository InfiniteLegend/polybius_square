import random
import math


def is_prime(number):
    """
    Returns True if number is prime, return False if - composite.
    :param number:
    :return:
    """
    i = 2
    j = 0
    while i <= math.sqrt(number) and j != 1:
        if number % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


def primes(n, m):
    """
    Returns list of prime numbers [n:m].
    :param n:
    :param m:
    :return:
    """
    prime_list = []
    for number in xrange(n, m+1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list


def are_relatively_prime(a, b):
    """Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.

    Two numbers are relatively prime if they share no common factors,
    i.e. there is no integer (except 1) that divides both.
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def random_prime(bits):
    """
    Returns random prime number bit long - bits.
    :param bits:
    :return:
    """
    n_min = 1 << (bits - 1)
    n_max = (1 << bits) - 1

    start = 1 << (bits // 2 - 1)
    stop = 1 << (bits // 2 + 1)

    # primes_list = get_primes(start, stop)
    primes_list = primes(start, stop)
    while primes_list:
        p = random.choice(primes_list)
        primes_list.remove(p)
        q_candidates = [q for q in primes_list
                        if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise AssertionError("cannot find 'p' and 'q' for a key of "
                             "length={!r}".format(bits))
    stop = (p - 1) * (q - 1)
    for e in xrange(3, stop, 2):
        if are_relatively_prime(e, stop):
            break
    else:
        raise AssertionError("cannot find 'e' with p={!r} "
                             "and q={!r}".format(p, q))

    for d in xrange(3, stop, 2):
        if d * e % stop == 1:
            break
    else:
        raise AssertionError("cannot find 'd' with p={!r}, q={!r} "
                             "and e={!r}".format(p, q, e))

    # That's all. We can build and return the public and private keys.
    return [p * q, e, p * q, d]


def encrypt(encrypt_string, e, n):
    """
    Returns the encrypted string encrypt_string with public key (e, n).
    Result is to be reduced to an array of row: 123456,234567,345678 ...
    :param encrypt_string:
    :param e:
    :param n:
    :return:
    """


def decrypt(decrypt_string, d, n):
    """
    Decrypts the secret key (d, n).
    The result should be the source string to its encryption.
    :param decrypt_string:
    :param d:
    :param n:
    :return:
    """


import time


if __name__ == "__main__":
    start = time.time()
    test = random_prime(25)
    print(test)
    print("Time: %.03f s" % (time.time() - start))