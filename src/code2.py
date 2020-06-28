def expo(b, n):
    """
    Exponential function using recursion
    Calculate exponent
    Given the base b, and , a positive integer n
    computes b raised to the exponent n
    recurviely,

    if n is 0, return 1
    else, b * b^(b-1)
    """
    if n == 0:
        return 1
    else:
        return b * expo(b, n - 1)
