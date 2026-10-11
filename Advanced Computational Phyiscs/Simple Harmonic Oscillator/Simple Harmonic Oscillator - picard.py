import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return -k * y  # Equation for simple harmonic oscillator

def picard(x0, y0, h, n):
    x = [x0]
    y = [y0]
    
    for i in range(n):
        x.append(x[i] + h)  # Increment x by h each step
        
        y_new = y[i]
        for j in range(i):
            y_new += h * func(x[j], y[j])  # Iterate using previous y values
        
        y.append(y_new)
    
    return x, y

# Constants
k = 1.0  # Spring constant
x0 = 0.0  # Initial x position
y0 = 1.0  # Initial y position (amplitude)
h = 0.01  # Step size
n = 1000  # Number of iterations

# Solve using Picard method
x, y = picard(x0, y0, h, n)

# Plot the solution
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Solution of Simple Harmonic Oscillator')
plt.show()
