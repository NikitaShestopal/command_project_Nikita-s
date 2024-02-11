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

def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'
    binary_number = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2
    return binary_number
