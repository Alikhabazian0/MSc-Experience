"""
  Auther: Ali khabazian
  computational physics, physics group, IUST
  created on july 2023
"""
import numpy as np
import random
def init_spin_array(rows, cols):
    return np.ones((rows, cols))

def find_neighbors(spin_array, lattice, x, y):
    left   = (x, y - 1)
    right  = (x, (y + 1) % lattice)
    top    = (x - 1, y)
    bottom = ((x + 1) % lattice, y)

    return [spin_array[left[0], left[1]],
            spin_array[right[0], right[1]],
            spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]]]

#calculating the energy of the configuration
def energy(spin_array, lattice, x ,y):
    return 2 * spin_array[x, y] * sum(find_neighbors(spin_array, lattice, x, y))

def main10():
    RELAX_SWEEPS =10
    lattice = 10
    sweeps =190
    e1= e0 = 0
    temperatures=[1,3]
    for temperature in temperatures:
        
     spin_array = init_spin_array(lattice, lattice)
     M= np.zeros(sweeps + RELAX_SWEEPS)
     
     A=[]
     for sweep in range(sweeps + RELAX_SWEEPS):
            for i in range(lattice):
                for j in range(lattice):
                    e = energy(spin_array, lattice, i, j)
                    if e <= 0:
                        spin_array[i, j] *= -1
                    elif np.exp((-1.0 * e)/temperature) > random.random():
                        spin_array[i, j] *= -1

             

            #Magnetization
            M[sweep] = abs(sum(sum(spin_array)))
            A.append(M[sweep])
    
     print("all magnets=",A)  
     c=sum(A)
     print("average of Magnets =",c/200)
            
main10()
