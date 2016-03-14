

def is_prime(number):
    """
    Returns True if number is prime, return False if - composite.
    :param number:
    :return:
    """
    i = 2
    j = 0
    while i ** 2 <= number and j != 1:
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


def random_prime(bits):
    """
    Returns random prime number bit long - bits.
    :param bits:
    :return:
    """


def encrypt(encrypt_string, e, n):
    """
    Returns the encrypted string encrypt_string with public key (e, n).
    Result is to be reduced to an array of row: 123456,234567,345678 ...
    :param encrypt_string:
    :param e:
    :param n:
    :return:
    """


def decrypt(s, d, n):
    """
    Decrypts the secret key (d, n).
    The result should be the source string to its encryption.
    :param s:
    :param d:
    :param n:
    :return:
    """