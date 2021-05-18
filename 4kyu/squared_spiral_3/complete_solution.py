import math


def squared_spiral(n):

    sqrt = math.floor(math.sqrt(n))
    remaining = n - (sqrt ** 2)

    if sqrt % 2 == 0:
        x = -int(sqrt / 2) + max(remaining - sqrt, 0)
        y = int(sqrt / 2) - min(remaining, sqrt)

    else:
        x = math.ceil(sqrt / 2) - max(remaining - sqrt, 0)
        y = -math.floor(sqrt / 2) + min(remaining, sqrt)

    return x, y
