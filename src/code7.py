# line segment problem


def makepoint(xcord, ycord):
    return [xcord, ycord]


def xpoint(p):
    return p[0]


def ypoint(p):
    return p[1]


def midpoint(point1, point2):
    """ make use of // """
    def avg(a, b):
        return (a + b) // 2

    xcord = avg(xpoint(point1), xpoint(point2))
    ycord = avg(ypoint(point1), ypoint(point2))

    return makepoint(xcord, ycord)


def printpoint(p):
    return f"({xpoint(p)}, {ypoint(p)})"
