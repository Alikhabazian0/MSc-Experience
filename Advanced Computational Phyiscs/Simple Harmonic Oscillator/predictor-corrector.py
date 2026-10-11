import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator(x0, v0, k, m, t_end, dt):
    # Initialize arrays to store position and velocity
    t = np.arange(0, t_end + dt, dt)
    num_steps = len(t)
    x = np.zeros(num_steps)
    v = np.zeros(num_steps)

    # Set initial conditions
    x[0] = x0
    v[0] = v0

    # Predictor-Corrector method
    for i in range(1, num_steps):
        # Predictor step
        x_pred = x[i-1] + dt * v[i-1]
        v_pred = v[i-1] - dt * (k/m) * x[i-1]
        
        # Corrector step
        x[i] = x[i-1] + dt * 0.5 * (v[i-1] + v_pred)
        v[i] = v[i-1] - dt * 0.5 * (k/m) * (x[i-1] + x_pred)

    return t, x, v

# Parameters
x0 = 1.0  # Initial position
v0 = 0.0  # Initial velocity
k = 1.0   # Spring constant
m = 1.0   # Mass
t_end = 10.0  # End time
dt = 0.01    # Time step

# Solve the differential equation
t, x, v = harmonic_oscillator(x0, v0, k, m, t_end, dt)

# Plot the position and velocity as functions of time
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Position vs Time')

plt.subplot(1, 2, 2)
plt.plot(t, v)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity vs Time')

plt.tight_layout()
plt.show()
