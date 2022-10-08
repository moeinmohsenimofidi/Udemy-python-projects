import math


def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon


print(assertEquals(sqrt(4), 2))
print(assertEquals(sqrt(9), 3))
print(assertEquals(sqrt(100), 10))