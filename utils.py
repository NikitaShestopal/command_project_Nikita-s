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
