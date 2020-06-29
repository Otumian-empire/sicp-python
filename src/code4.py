# write a procedure that takes a and b as argument and returns the sum
# from a to b, inclusive. return 0, when a < b


# because of the recursion limit in python
# let the b be less than 1000
def sum_integer_recursion(a, b):
    """
    returns the sum from a to b, inclusive.
    given a = 1, b = 3, returns 1 + 2 + 3 = 6
    """
    r = 0
    if a <= b:
        r = a + sum_integer_recursion(a + 1, b)
    return r


def sum_integer_loop(a, b):
    """
    returns the sum from a to b, inclusive.
    given a = 1, b = 3, returns 1 + 2 + 3 = 6
    """
    sum_t = 0

    while (a <= b):
        sum_t += a
        a += 1

    return sum_t
