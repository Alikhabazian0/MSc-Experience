"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np

def f(x, y, a, b):
    return np.sin(a * x + np.pi/4) * np.cos(b * x) * np.sqrt(a * y**2 + b**2 * x + 1)

def simpson_2d(f, a, b, n):
    assert(n % 2 == 0)
    h = (b - a) / n
    s = 0.0
    for i in range(0, n, 2):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        x3 = a + (i + 2) * h
        for j in range(0, n, 2):
            y1 = a + j * h
            y2 = a + (j + 1) * h
            y3 = a + (j + 2) * h
            s += (h**2 / 9) * (f(x1, y1, a, b) + 4 * f(x2, y1, a, b) + f(x3, y1, a, b) +
                               4 * (f(x1, y2, a, b) + 4 * f(x2, y2, a, b) + f(x3, y2, a, b)) +
                               f(x1, y3, a, b) + 4 * f(x2, y3, a, b) + f(x3, y3, a, b))
    return s

a = np.pi / 2
b = 0
n = int(input("Enter the value of n: "))

result = simpson_2d(f, a, b, n)
print("Simpson's 1/3 method result:", result)
