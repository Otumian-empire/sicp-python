def f(n):
    """
    returns n if n is less than 3 else returns f(n - 1) + (2 * f(n - 2)) + (3 * f(n - 3))
    """
    if n < 3:
        return n
    else:
        return f(n - 1) + (2 * f(n - 2)) + (3 * f(n - 3))
