import random
import math
import time


def FindPrimes_1(start, limit):
    IsPrimes = []
    sqrt = math.sqrt(limit)

    x = 1
    while x <= sqrt:
        y = 1
        while y <= sqrt:
            # for y in xrange(1, sqrt):
            x2 = x * x
            y2 = y * y
            n = 4 * x2 + y2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                IsPrimes.append(n)

            n -= x2
            if n <= limit and n % 12 == 7:
                IsPrimes.append(n)

            n -= 2 * y2
            if x > y and n <= limit and n % 12 == 11:
                IsPrimes.append(n)
                # IsPrimes[n] = IsPrimes.get(n, False) ^ True
            y += 1
        x += 1
    n = 5
    while n <= sqrt:
        if n in IsPrimes:
            s = n * n
            for k in xrange(s, limit, s):
                if k in IsPrimes:
                    IsPrimes.remove(k)
        n += 2
    # IsPrimes[2] = True
    # IsPrimes[3] = True
    IsPrimes = [el for el in IsPrimes if el >= start]
    return IsPrimes


def FindPrimes(start, limit):
    IsPrimes = []
    sqrt = math.sqrt(limit)
    # for x in xrange(1, sqrt):
    x = 1
    while x <= sqrt:
        y = 1
        while y <= sqrt:
            # for y in xrange(1, sqrt):
            x2 = x * x
            y2 = y * y
            n = 4 * x2 + y2

            if n <= limit and (n % 12 == 1 or n % 12 == 5) and n >= start:
                IsPrimes.append(n)

            n -= x2
            if n <= limit and n % 12 == 7 and n >= start:
                IsPrimes.append(n)

            n -= 2 * y2
            if x > y and n <= limit and n % 12 == 11 and n >= start:
                IsPrimes.append(n)
                # IsPrimes[n] = IsPrimes.get(n, False) ^ True
            y += 1
        x += 1
    n = 5
    while n <= sqrt:
        if n in IsPrimes:
            s = n * n
            for k in xrange(s, limit, s):
                IsPrimes.pop(k)
        n += 2
    # IsPrimes[2] = True
    # IsPrimes[3] = True
    return IsPrimes


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
    for number in xrange(n, m + 1):
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
    # start_time = time.time()
    primes_list = FindPrimes(start, stop)
    # primes_list = FindPrimes_1(start, stop)
    # print("Anki Time: %.03f s" % (time.time() - start_time))

    # start_time = time.time()
    # primes_list = primes(start, stop)
    # print("Default Time: %.03f s" % (time.time() - start_time))

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
    return p, q


def get_keys(length):
    p, q = random_prime(length)
    stop = (p - 1) * (q - 1)  # Eler function
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
    n = p * q
    # That's all. We can build and return the public and private keys.
    return {'e': e, 'n': n}, {'d': d, 'n': n}


def encrypt(encrypt_string, e, n):
    """
    Returns the encrypted string encrypt_string with public key (e, n).
    Result is to be reduced to an array of row: 123456,234567,345678 ...
    :param encrypt_string:
    :param e:
    :param n:
    :return:
    """
    # cript_list = []
    # for item in list(str(encrypt_string)):
    #     cript_list.append(pow(int(item), e, n))
    # return cript_list
    return pow(encrypt_string, e, n)


def decrypt(decrypt_string, d, n):
    """
    Decrypts the secret key (d, n).
    The result should be the source string to its encryption.
    :param decrypt_string:
    :param d:
    :param n:
    :return:
    """
    # cript_list = []
    # for item in decrypt_string:
    #     cript_list.append(pow(item, d, n))
    # return int(''.join(map(str, cript_list)))
    return pow(decrypt_string, d, n)



if __name__ == "__main__":
    start = time.time()
    pub_key, priv_key = get_keys(30)
    cript = encrypt(1234567, pub_key['e'], pub_key['n'])
    print(cript)
    mes = decrypt(cript, priv_key['d'], priv_key['n'])
    print(mes)
    print("Time: %.03f s" % (time.time() - start))
