def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def is_power_of_five(number):
    import math
    return (number > 0) and (math.log(number, 5) % 1 == 0)
