import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Using pandas to read data
data_x = pd.read_csv("x_new.txt", delimiter=' ', header=None, names=['index', 'x', 'delta_x'])
data_y = pd.read_csv("y_new.txt", delimiter=' ', header=None, names=['index', 'y', 'delta_y'])

x = data_x['x']
delta_x = data_x['delta_x']
y = data_y['y']
delta_y = data_y['delta_y']

z = np.tanh(x**2) + np.exp(y)
delta_z = np.sqrt(((2*x/(np.cosh(x**2)*np.sin(x**2)))*delta_x)**2 + ((y)*delta_y)**2)

error_limit = 10 
limited_delta_z = np.clip(delta_z, a_min=None, a_max=error_limit)

plt.figure(figsize=(12, 4), dpi=500)
plt.errorbar(data_x['index'], z, yerr=limited_delta_z, capsize=5, fmt='.', label=r'$ \sigma_{\mathbf{Z}} =\sqrt{(\frac{\partial \mathbf{Z}}{\partial x_i } \sigma_{x_i})^2 + (\frac{\partial \mathbf{Z}}{\partial y_i} \sigma_{y_i})^2 }  $')
plt.plot(data_x['index'], z, label=r'$ \mathbf{Z} = \tanh {x^2} + e^y $')
plt.xlabel('time point')
plt.ylabel(r'$ \mathbf{Z} $')
plt.tick_params(direction='in')
plt.legend()
plt.show()
