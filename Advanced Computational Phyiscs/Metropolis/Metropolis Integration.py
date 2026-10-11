import numpy as np

def integrand(v, b, m):
    return np.exp(-(b * m / 2) * (v ** 2))

def metropolis_integration(b, m, num_samples, proposal_std=1.0):
    np.random.seed(42)  
    
    v = 0.0
    integral_sum = 0.0
    accepted_samples = 0
    
    for _ in range(num_samples):
        
        v_prime = np.random.normal(loc=v, scale=proposal_std)
        
        acceptance_ratio = integrand(v_prime, b, m) / integrand(v, b, m)
        
        u = np.random.uniform(0, 1)
        
        if u < acceptance_ratio:
            v = v_prime
            accepted_samples += 1
        
        integral_sum += integrand(v, b, m)
    
    integral_estimate = integral_sum / num_samples
    
    return integral_estimate, accepted_samples

b = 2.0
m = 1.0
num_samples = 1000000

integral_estimate, accepted_samples = metropolis_integration(b, m, num_samples)

exact_result = np.sqrt(2 * np.pi / (b * m))

print("Metropolis method estimate:", integral_estimate)
print("Exact result:", exact_result)
print("Number of accepted samples:", accepted_samples)