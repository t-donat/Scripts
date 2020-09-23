import math


def prime_numbers_v1(n):
    """Checks if 'n' is a prime number. Returns 'True' if it is, returns 'False' if not."""

    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def prime_numbers_v2(n):
    """Checks if 'n' is a prime number. Returns 'True' if it is, returns 'False' if not."""

    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(2, max_divisor+1):

        if n % d == 0:
            return False

    return True


def prime_numbers_v3(n):
    """Checks if 'n' is a prime number. Returns 'True' if it is, returns 'False' if not."""

    if n == 1:
        return False

    # All numbers divisible by 2 except for 2 itself aren't prime numbers, checking them all would be unnecessary
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, max_divisor+1, 2):
        if n % d == 0:
            return False

    return True

# bool_prime_1_to_10 = [False, True, True, False, True, False, True, False, False, False]
# bool_prime_11_to_20 = [True, False, True, False, False, False, True, False, True, False]
# bool_prime_21_to_30 = [False, False, True, False, False, False, False, False, True, False]

# for index, element in enumerate(bool_prime_1_to_10 + bool_prime_11_to_20 + bool_prime_21_to_30):
#    n = index + 1
#    result = prime_numbers_v2(n)

#    print(f"{n}: result: {result}, expected: {element}, correct: {result == element}")



