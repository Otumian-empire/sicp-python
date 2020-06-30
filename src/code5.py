"""
write a procedure for f(x, y)= x(1+xy)^2 + y(1-y) + (1+xy)(1-y)

f(x, y)= x(1+xy)^2 + y(1-y) + (1+xy)(1-y)

a = (1 + xy)
b = (1 - y)
fr(a, b) = xa^2 + yb + ab
"""


""" 
def f(x, y):
    def fr(a, b):
        return (x * (a ** 2)) + (y * b) + (a * b)

    return fr((1 + (x * y)), (1 - y))
 """


def f(x, y):
    a = (1 + (x * y))
    b = (1 - y)
    return (x * (a ** 2)) + (y * b) + (a * b)
