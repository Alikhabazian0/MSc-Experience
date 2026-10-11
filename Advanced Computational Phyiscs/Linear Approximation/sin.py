import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = sin(x^2)
def f(x):
    return np.sin(x**2)

# Generate x values in the interval [0, 3]
x = np.linspace(0, 3, 300)

# Calculate corresponding y values
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = sin(x^2)", color="blue")
plt.title("Plot of f(x) = sin(x^2)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
