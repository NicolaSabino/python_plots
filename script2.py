import numpy as np
import matplotlib.pyplot as plt 
import random

time = np.arange(0, 3, 0.00001)
fx = []
for x in time:
    fx.append(x**3 - 3*x**3 + 5*x**2 + 2*x + 1)


'''func = time * np.cos(np.pi/time)
func2 = np.pi * (np.sin(np.pi * time) - np.sin(2 * np.pi * time)) / 2 /2
func3 = np.power(time,3)
plt.plot(time,fx)
plt.show()'''


vec = np.array([-5,0,5],dtype=float)
print(np.interp(vec, (vec.min(), vec.max()), (-1, +1)))