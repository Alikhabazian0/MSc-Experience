import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system equations
def lorenz(t, xyz):
    x, y, z = xyz
    dx_dt = 10 * (y - x)
    dy_dt = -x * z + 28 * x - y
    dz_dt = x * y - (8/3) * z
    return [dx_dt, dy_dt, dz_dt]

# Set the initial conditions
x0, y0, z0 = [1.0, 1.0, 1.0]
initial_conditions = [x0, y0, z0]

# Set the time span
t_start = 0.0
t_end = 50.0
num_points = 10000
t_span = np.linspace(t_start, t_end, num_points)

# Solve the Lorenz system
from scipy.integrate import solve_ivp
solution = solve_ivp(lorenz, [t_start, t_end], initial_conditions, t_eval=t_span)

# Extract the solution
x_values = solution.y[0]
y_values = solution.y[1]
z_values = solution.y[2]

# Plot the phase diagram
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Lorenz Attractor Phase Diagram')
plt.show()