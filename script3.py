import numpy as np
import matplotlib.pyplot as plt 
import random

def cubic_values(x_vector, x_max, x_min, y_max):
    '''
        Implements the function 
        y =  ax^3 + bx^2 + c
        a = ((-2) * (x_max - x_min))/y_max^3
        b = (3 * (x_max - x_min))/y_max ^2
        c = 0
    '''
    
    a = ((-2) * (x_max - x_min))/pow(y_max,3)
    b = (3 * (x_max - x_min))/pow(y_max,2)
    c = 0

    return [(a*(x**3))+(b*(x**2))+c for x in x_vector]

def gen_time(maxTime):
    tick = 1
    tick_perid = 50
    milli = 1000
    result_vector = [x for x in np.arange(0,maxTime,0.05)]
    return result_vector

if __name__ == "__main__":

    ref_brake = [0.00725, 0.028, 0.06075, 0.104, 0.15625, 0.216, 0.28175, 0.352, 0.42525, 0.5,
     0.57475, 0.648, 0.71825, 0.784, 0.84375, 0.896, 0.93925, 0.972, 0.99275, 1]

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

    ref_steer = [
					    0.362593,
					    1.43407,	
					    3.19,	
					    5.60593,	
					    8.65741,	
					    12.32,	
					    16.5693,	
					    21.3807,	
					    26.73,	
					    32.5926,	
					    38.9441,	
					    45.76,	
					    53.0159,	
					    60.6874,	
					    68.75,	
					    77.1793,	
					    85.9507,	
					    95.04,	
					    104.423,	
					    114.074,	
					    123.97,	
					    134.086,	
					    144.397,	
					    154.88,	
					    165.509,	
					    176.261,	
					    187.11,	
					    198.033,	
					    209.004,	
					    220	,
                        230.996,	
					    241.967,	
					    252.89,	
					    263.739,	
					    274.491,	
					    285.12,	
					    295.603,	
					    305.914,	
					    316.03,	
					    325.926,	
					    335.577,	
					    344.96,	
					    354.049,	
					    362.821,	
					    371.25,	
					    379.313,	
					    386.984,	
					    394.24,	
					    401.056,	
					    407.407,	
					    413.27,	
					    418.619,	
					    423.431,	
					    427.68,	
					    431.343,	
					    434.394,	
					    436.81,	
					    438.566,	
					    439.637,	
					    440.0
    ]

    max_brake_duration = 1.01
    max_brake_intensity = 1
    max_time_steering = 3
    max_steering_angle = 440.0

    time = [x for x in np.arange(-0.25,1.25,0.01)]
    time2 = [x for x in np.arange(0,max_brake_duration+0.001,max_brake_duration/20)]

    steering_vector = []
    brake_vector = []
    brake_vector2 = []

    fig, ax = plt.subplots()
    brake_vector = cubic_values(
        x_vector=time,
        x_max=1,
        x_min=0,
        y_max=1
    )
    brake_vector2 = cubic_values(
        x_vector=time2,
        x_max=1,
        x_min=0,
        y_max=1
    )

    steering_vector = cubic_values(
        x_vector=time,
        x_max=440.0,
        x_min=0,
        y_max=3
    )
    steering_vector2 = cubic_values(
        x_vector=time2,
        x_max=440.0,
        x_min=0,
        y_max=3
    )

    #ax.plot(time, brake_vector,linewidth=0.75,linestyle='--',label='Curve interpolation')
    #ax.scatter(time2, brake_vector2,marker='o',color='orange', label='Brake values')


    ax.plot(range(len(ref_steeringAngles)),ref_steeringAngles)
    #ax.plot(time, steering_vector,linewidth=0.75,linestyle='--',label='curve interpolation')
    #ax.scatter(time2, steering_vector2,marker='o',color='orange', label='brake values')
    #time = gen_time(max_time_steering)
    #ax.plot(time, ref_steer)
    #ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
    ax.set_ylabel('intensity')
    ax.set_xlabel('time')
    ax.grid()
    ax.legend()

    #fig.savefig("test.png")
    plt.show()

    #print(steering_vector)
    #print(brake_vector)
