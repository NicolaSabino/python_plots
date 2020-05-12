import numpy as np
import matplotlib.pyplot as plt
import random

ref_steeringAngles = [0.81125, 3.19, 7.05375, 12.32, 18.9063, 26.73, 35.7087, 45.76, 56.8012, 68.75,
                      81.5237, 95.04, 109.216, 123.97, 139.219, 154.88, 170.871, 187.11, 203.514, 220, 236.486, 252.89,
                      269.129, 285.12, 300.781, 316.03, 330.784, 344.96, 358.476, 371.25, 383.199, 394.24, 404.291,
                      413.27, 421.094, 427.68, 432.946, 436.81, 439.189, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 440.0, 439.189, 436.81,
                      432.946, 427.68, 421.094, 413.27, 404.291, 394.24, 383.199, 371.25, 358.476, 344.96, 330.784, 316.03,
                      300.781, 285.12, 269.129, 252.89, 236.486, 220, 203.514, 187.11, 170.871, 154.88, 139.219, 123.97,
                      109.216, 95.04, 81.5237, 68.75, 56.8012, 45.76, 35.7087, 26.73, 18.9063, 12.32, 7.05375, 3.19,
                      0.81125]

max_brake_duration = 1.01
max_brake_intensity = 1
max_time_steering = 3
max_steering_angle = 440.0

time = np.arange(start=0, stop=9, step=float(9)/float(len(ref_steeringAngles)))
print(time)
print(ref_steeringAngles)

fig, ax = plt.subplots()
#ax.plot(time, ref_steeringAngles)
ax.plot(time, ref_steeringAngles,linewidth=0.75,linestyle='--',label='Curve interpolation')
ax.scatter(time, ref_steeringAngles,marker='o',color='orange', label='steering values')

ax.axvspan(0,2,color='red', alpha=0.1)
ax.axvspan(2,7,color='blue', alpha=0.1)
ax.axvspan(7,9,color='red', alpha=0.1)
ax.set_ylabel('steering angle (°)',fontsize=14)
ax.set_xlabel('time', fontsize=14)
ax.text(0.5, 0, 'steering duration ', fontsize=14)
ax.text(3.75, 0, 'const steering time', fontsize=14)
ax.text(7.25, 0, 'steering duration', fontsize=14)
ax.grid()
ax.legend()
plt.show()
