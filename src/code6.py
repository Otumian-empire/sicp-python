# design a system that performs arithmetic with rational numbers


def num_rat(r):
    """ return the numerator of a given rational number """
    return r[0]


def denum_rat(r):
    """ return the denominator of a given rational number """
    return r[1]


def make_rat(n, d):
    """ return a rational number of two given numbers as the numerator and the denominator of type list"""
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    g = gcd(n, d)

    return [int(n/g), int(d/g)]


def add_rat(x, y):
    """ adds rational numbers """
    return make_rat(
        (num_rat(x) * denum_rat(y)) + (denum_rat(x) * num_rat(y)),
        denum_rat(x) * denum_rat(y)
    )


def sub_rat(x, y):
    """ subtracts rational numbers """
    return make_rat(
        (num_rat(x) * denum_rat(y)) - (denum_rat(x) * num_rat(y)),
        denum_rat(x) * denum_rat(y)
    )


def mul_rat(x, y):
    """ multiplies rational numbers """
    return make_rat(
        num_rat(x) * num_rat(y),
        denum_rat(x) * denum_rat(y)
    )


def div_rat(x, y):
    """ divides rational numbers """
    return make_rat(
        num_rat(x) * denum_rat(y),
        denum_rat(x) * num_rat(y)
    )


def eq_rat(x, y):
    """ check for equality of rational numbers """
    return (num_rat(x) * denum_rat(y)) == (denum_rat(x) * num_rat(y))


def print_rat(r):
    """ returns a string-like fraction of a given rational number """
    return f"{num_rat(r)}/{denum_rat(r)}"

