import numpy as np


def rnd1(high):
    """
    return random int in range [1, high]
    """
    return np.random.randint(1, high + 1)


def rnd0(high):
    """
    return random int in range [0, high]
    """
    return np.random.randint(0, high + 1)
