"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(func, r, t, h):
    k1 = h * func(r, t)
    k2 = h * func(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * func(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * func(r + k3, t + h)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6

mo = float(input("Enter a value for mo: "))

def vanderPolFunction(r, t):
    x, v = r[0], r[1]
    fx = v
    fv = -x + mo * (1 - x**2) * v
    return np.array([fx, fv], float)

tMin, tMax = 0.0, 20.0
nSteps = 1000
tStep = (tMax - tMin) / nSteps

tPoints = np.arange(tMin, tMax, tStep)
xPoints, vPoints = [], []
x0 = float(input("Enter the initial position: "))
v0 = float(input("Enter the initial velocity: "))
r = np.array([x0, v0], float)

for t in tPoints:
    xPoints.append(r[0])
    vPoints.append(r[1])
    r += runge_kutta4(vanderPolFunction, r, t, tStep)

plt.plot(xPoints, vPoints)
plt.ylabel("x")
plt.xlabel("dx/dt")
plt.show()
