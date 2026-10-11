import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Hamiltonian
def calculate_hamiltonian(network, q=1):
    N = len(network)
    H = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                H -= network[i, j] * network[j, k] * network[k, i]
    return H

# Function to update network based on Metropolis algorithm
def update_network(network, T, q=1):
    N = len(network)
    i, j = np.random.randint(0, N, size=2)
    i, j = min(i, j), max(i, j)
    
    old_H = calculate_hamiltonian(network, q)
    network[i, j] *= -1
    network[j, i] *= -1
    new_H = calculate_hamiltonian(network, q)
    
    delta_H = new_H - old_H
    if delta_H < 0:
        return network
    else:
        if np.random.rand() < np.exp(-delta_H / T):
            return network
        else:
            network[i, j] *= -1
            network[j, i] *= -1
            return network

# Simulation parameters
N = 50
T_values = [10, 12, 14, 16, 18, 20]
n_steps = 1600
q = 1

# Initialize networks
networks = {T: np.random.choice([-1, 1], size=(N, N)) for T in T_values}
for T in T_values:
    networks[T] = (networks[T] + networks[T].T) * (networks[T] > 0)

# Run simulations
results = {T: [] for T in T_values}
for step in range(n_steps):
    for T in T_values:
        networks[T] = update_network(networks[T], T, q)
        mean_triad_energy = calculate_hamiltonian(networks[T], q) / (N * (N - 1) * (N - 2) / 6)
        results[T].append(-mean_triad_energy)

# Plot results
plt.figure(figsize=(8, 6))
for T in T_values:
    plt.plot(range(n_steps), results[T], label=f'T={T}')
plt.xlabel('Monte Carlo steps (n)')
plt.ylabel('-<SikSkjSji>')
plt.title('Mean triad energy vs Monte Carlo steps for different temperatures')
plt.legend()
plt.show()