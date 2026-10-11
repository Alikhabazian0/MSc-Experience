"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
from scipy.integrate import solve_ivp

def potential(x, a, l):
    if np.abs(x) <= l:
        return a * x**2
    else:
        return np.inf

def schrodinger_eq(x, psi, a, l, E):
    return np.array([psi[1], (2 * potential(x, a, l) - E) * psi[0]])

def solve_schrodinger_eq(a, l, E):
    x_span = (-l, l)
    psi_initial = [0.0, 1.0]  # Initial conditions: psi(0) = 0, psi'(0) = 1
    solution = solve_ivp(lambda x, psi: schrodinger_eq(x, psi, a, l, E), x_span, psi_initial)
    return solution.y[0][-1]

def find_eigenvalues(a, l, num_eigenvalues):
    eigenvalues = []
    E = 0.01  # Start with a small energy
    while len(eigenvalues) < num_eigenvalues:
        E += 0.1  # Energy increment
        psi_right = solve_schrodinger_eq(a, l, E)
        if np.abs(psi_right) < 0.01:  # Check if the wavefunction vanishes at the right boundary
            eigenvalues.append(E)
    return eigenvalues

a = 0
l = 1
num_eigenvalues = 5

eigenvalues = find_eigenvalues(a, l, num_eigenvalues)
for i, eigenvalue in enumerate(eigenvalues):
    print(f"Eigenvalue {i+1}: {eigenvalue}")
