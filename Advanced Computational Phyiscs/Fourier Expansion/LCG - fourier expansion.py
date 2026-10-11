import numpy as np
import matplotlib.pyplot as plt

def lcg_random_numbers(seed, a, c, m, count):
    numbers = []
    x = seed
    for _ in range(count):
        x = (a * x + c) % m
        numbers.append(x)
    return numbers

def fourier_expansion(data, n):
    coefficients = np.fft.fft(data)
    coefficients[n+1:] = 0 
    reconstructed_data = np.fft.ifft(coefficients)
    return np.real(reconstructed_data)

def replace_random_numbers(data, indices, min_val, max_val):
    new_data = data.copy()
    for index in indices:
        new_data[index] = np.random.uniform(min_val, max_val)
    return new_data

seed = 0
a = 1664525
c = 1013904223
m = 2**32 - 1
data = lcg_random_numbers(seed, a, c, m, 730)  

# Part a)
n_values = [1, 2, 4, 8, 16, 32]
for n in n_values:
    reconstructed_data = fourier_expansion(data, n)
    plt.plot(data, label='Initial Data')
    plt.plot(reconstructed_data, label=f'n = {n}')
    plt.legend()
    plt.show()

# Part b)
indices = [100, 200, 300, 400]
min_val = min(data)
max_val = max(data)
modified_data = replace_random_numbers(data, indices, min_val, max_val)
for n in n_values:
    reconstructed_data = fourier_expansion(modified_data, n)
    plt.plot(modified_data, label='Modified Data')
    plt.plot(reconstructed_data, label=f'n = {n}')
    plt.legend()
    plt.show()