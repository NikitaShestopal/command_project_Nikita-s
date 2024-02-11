def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def nsd(a: int, b: int):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    if b == 0:
        return a

    return nsd(b, a % b)


def is_power_of_five(number):
    import math
    return (number > 0) and (math.log(number, 5) % 1 == 0)


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

