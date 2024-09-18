import math


def McCormick(x1: float, x2: float) -> float:
    return math.sin(x1 + x2) + (x1 - x2) ** 2 - 1.5 * x1 + 2.5 * x2
