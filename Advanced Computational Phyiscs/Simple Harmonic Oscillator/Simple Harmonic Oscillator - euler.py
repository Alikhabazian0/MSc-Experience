import numpy as np
import matplotlib.pyplot as plt

def simple_harmonic_oscillator(k, m, x0, v0, dt, num_steps):
    # Initialize arrays to store position and velocity
    x = np.zeros(num_steps)
    v = np.zeros(num_steps)
    
    # Set initial conditions
    x[0] = x0
    v[0] = v0
    
    # Perform Euler method for each time step
    for i in range(1, num_steps):
        # Calculate new position and velocity
        x[i] = x[i-1] + v[i-1] * dt
        v[i] = v[i-1] - (k/m) * x[i-1] * dt
    
    return x, v

# Parameters
k = 1.0    # Spring constant
m = 1.0    # Mass
x0 = 1.0   # Initial position
v0 = 0.0   # Initial velocity
dt = 0.01  # Time step size
num_steps = 1000  # Number of time steps

# Solve the differential equation
x, v = simple_harmonic_oscillator(k, m, x0, v0, dt, num_steps)

# Plot the position vs. time
t = np.linspace(0, dt * num_steps, num_steps)
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Simple Harmonic Oscillator')
plt.show()
