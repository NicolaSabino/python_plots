import numpy as np
import matplotlib.pyplot as plt 
import random

def normalize(array):
    vec = np.array(array,dtype=float)
    return np.interp(vec, (vec.min(), vec.max()), (-1, +1))



# from 0 to 10, step 0.00001
time = np.arange(0, 3, 0.0001)
frequencies = [
    [32, 100],
    [13, 32],
    [8, 13],
    [4, 8],
    [1, 4]
]

non_periodic_function = []
for x in time:
    non_periodic_function.append(x**3 - 3*x**3 + 5*x**2 + 2*x + 1)


fig, axs = plt.subplots(5, sharex=True, sharey=True, gridspec_kw={'hspace': 0.5})
#fig.suptitle('Human Brainwaves')
axs[0].set_title('Gamma 32 - 100 Hz', fontsize=18)
axs[1].set_title('Beta 13 - 32 Hz', fontsize=18)
axs[2].set_title('Alpha 8 - 13 Hz', fontsize=18)
axs[3].set_title('Theta 4 - 8 Hz',fontsize=18)
axs[4].set_title('Delta 0.5 - 4 Hz',fontsize=18)
plt.xlabel('time')

counter = 0
for ranges in frequencies:
    new_wave = np.zeros(time.size)
    for i in range(20):
        freq = random.randrange(ranges[0],ranges[1])
        phase = random.random() * 2 * np.pi
        tmp =  np.sin(2 * np.pi * freq * time + phase)
        new_wave += tmp 
    new_wave *= non_periodic_function
    print(new_wave)
    new_wave = normalize(new_wave)
    print(new_wave)
    axs[counter].plot(time,new_wave,color='black', lw='1')
    counter += 1

plt.show()

