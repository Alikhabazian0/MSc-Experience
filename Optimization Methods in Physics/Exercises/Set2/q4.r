import numpy as np
import matplotlib.pyplot as plt

def compute_sigma_tao(data, tao):
    N = len(data)
    M = int(N / tao)
    sigma_tao = np.zeros(N-tao+1)

    for i in range(M):
        x_i = data[i*tao : (i+1)*tao]
        x_i_mean = np.mean(x_i)
        sigma_i = (1/tao) * np.sum((x_i - x_i_mean)**2)
        sigma_tao += sigma_i
    
    sigma_tao /= M
    return sigma_tao

# Task A
fbm_data = np.loadtxt("C:\\Users\\user\\OneDrive\\Desktop\\FBM.txt")
tao_values = np.arange(1, len(fbm_data)+1)
sigma_tao_fbm = compute_sigma_tao(fbm_data, tao_values)

# Task B
fgn_data = np.loadtxt("C:\\Users\\user\\OneDrive\\Desktop\\FGN.txt")
sigma_tao_fgn = compute_sigma_tao(fgn_data, tao_values)

# Task C
increment_data = np.diff(fbm_data)
sigma_tao_increment = compute_sigma_tao(increment_data, tao_values[:-1])

# Task D
profile_data = np.cumsum(fgn_data)
sigma_tao_profile = compute_sigma_tao(profile_data, tao_values)

# Task E
data_files = ["FBM_0.100", "FBM_0.300", "FBM_0.500", "FBM_0.700", "FBM_0.900","FGN_0.100", "FGN_0.300", "FGN_0.500", "FGN_0.700", "FGN_0.900"]
tao_stationary_values = []

for file in data_files:
    data = np.loadtxt(file)
    sigma_tao = compute_sigma_tao(data, tao_values)
    tao_stationary = np.argmax(sigma_tao) + 1
    tao_stationary_values.append(tao_stationary)

plt.figure(figsize=(10, 6))

# Task A
plt.subplot(2, 2, 1)
plt.plot(tao_values, sigma_tao_fbm)
plt.title("FBM.txt - sigma(tao)")
plt.xlabel("tao")
plt.ylabel("sigma(tao)")

# Task B
plt.subplot(2, 2, 2)
plt.plot(tao_values, sigma_tao_fgn)
plt.title("FGN.txt - sigma(tao)")
plt.xlabel("tao")
plt.ylabel("sigma(tao)")

# Task C
plt.subplot(2, 2, 3)
plt.plot(tao_values[:-1], sigma_tao_increment)
plt.title("Increment of FBM.txt - sigma(tao)")
plt.xlabel("tao")
plt.ylabel("sigma(tao)")

# Task D
plt.subplot(2, 2, 4)
plt.plot(tao_values, sigma_tao_profile)
plt.title("Profile of FGN.txt - sigma(tao)")
plt.xlabel("tao")
plt.ylabel("sigma(tao)")

plt.tight_layout()

# Task E
plt.figure(figsize=(10, 4))
plt.plot(data_files, tao_stationary_values, 'o-')
plt.title("Stationary Intensity")
plt.xlabel("Data Set")
plt.ylabel("tao_stationary")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()