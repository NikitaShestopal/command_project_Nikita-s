def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
<<<<<<< HEAD


def is_power_of_five(number):
    import math
    return (number > 0) and (math.log(number, 5) % 1 == 0)
=======
    
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
>>>>>>> 80459f2d960441a6f8445dbb917fbcb82ae5bd66
