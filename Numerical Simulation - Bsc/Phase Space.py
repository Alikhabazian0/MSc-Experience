"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
import matplotlib.pyplot as plt

# Set the time step
h = 0.01
t = np.arange(0, 1 + h, h)

# Input parameters
mo = float(input("Enter a value for mo: "))
x_initial = float(input("Enter the initial position: "))
v_initial = float(input("Enter the initial velocity: "))

# Define the function
def f(x, v):
    return mo * (1 - x ** 2) * v - x

# Initialize arrays
x = np.zeros(len(t))
v = np.zeros(len(t))
x[0] = x_initial
v[0] = v_initial

# Perform the numerical integration
for j in range(len(t) - 1):
    x[j + 1] = x[j] + v[j] * h
    v[j + 1] = v[j] + f(x[j], v[j]) * h

# Plot the results
plt.plot(v, x)
plt.xlabel('Velocity')
plt.ylabel('Position')
plt.title('Phase Space')
plt.show()
