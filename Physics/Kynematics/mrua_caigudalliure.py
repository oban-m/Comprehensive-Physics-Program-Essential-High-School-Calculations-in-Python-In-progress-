"""
    MRUA EN EL CAS QUE L'ACCELERACIO ES LA GRAVETAT
"""

import math
import matplotlib.pyplot as plt

g = -9.780

def question_high():
    while True:
        try:
            print("Write the high (in meters) where the mass is fallen.")
            high = float(input())
            if high >= 0:
                return high
            else:
                print("Hight must be positive or zero.")
        except ValueError:
            print('Write a correct value in meters.')

def question_v0():
    while True:
        try:
            print("Write the inicial velocity like a vector value.")
            v0 = float(input())
            return v0
        except ValueError:
            print("Write a correct value.")

def see_eq_mov(y0, v0):
    global g
    if y0 == 0:
        print(f"y(t) = {v0} * t + {1/2 * g} * t ** 2")
        pass
    elif v0 == 0:
        print(f"y(t) = {y0} + {1/2 * g} * t ** 2")
        pass
    else:
        print(f"y(t) = {y0} + {v0} * t + {1/2 * g} * t ** 2")
        pass

def see_eq_vel(v0):
    global g
    if v0 == 0:
        print(f"v(t) = {g} * t")
        pass
    else:
        print(f"y(t) = {v0} + {g} * t")
        pass

def pos_in_time(y0, v0, t):
    global g
    return y0 + v0 * t + 1/2 * g * t ** 2

def vel_in_time(v0, t):
    global g
    return v0 + g * t

def tiempo_caer(y0, v0):
    global g
    if y0> 0 and v0 == 0:
        return math.sqrt((2 * y0) / abs(g))
    else:
        print("Initial velocity must be zero and hight upper than zero.")
        pass

def max_hight(y0, v0):
    global g
    if y0 == 0 and v0 > 0:
        return v0 ** 2 / (2 * abs(g))
    else: 
        print("Velocity must be positive and hight zero.")
        pass

def grafica(y0, v0, t):
    global g
    times = [_ for _ in range(0, math.ceil(t)+1)]
    pos_y = list(map(lambda time: pos_in_time(y0, v0, time), times))
    velocities = list(map(lambda time: vel_in_time(v0, time), times))
    
    plt.figure()
    plt.plot(times, pos_y, label = 'high / time', color = 'blue')
    plt.plot(times, velocities, label = 'velocity / time', color = 'red')
    plt.xlabel("Hight and velocity.")
    plt.ylabel("Time")
    plt.title('Hight & Velocity / Time')
    plt.legend()
    plt.grid(True)
    plt.show()
    pass

def options():
    while True:
        try:
            print("What do you want to see:" 
                "1) Equation of the distance." 
                "2) Hight in a specific time." 
                "3) Equation of the velocity." 
                "4) Velocity in a specific time." 
                "5) Plot of the movement and velocity." 
                "6) Maximum hight if initial position is zero."
                "7) Time for mass to arrive to zero hight if initial velocity is zero and initial hight is positive."
            )
            ans = int(input())
            if ans not in [1, 2, 3, 4, 5, 6, 7]:
                print("Please, try again.")
            else:
                return ans
        except ValueError:
            print("Write a correct value.")

def entrada():
    while True:
        try:
            print("Write the inicial hight in meters.")
            high = float(input())
            print("Write the velocity in meters per second")
            vel = float(input())
            return high, vel
        except ValueError:
            print("Please write a correct number.")

def time():
    while True:
        try:
            print("Write the specific time.")
            time = float(input())
            if time >= 0:
                return time
            else:
                print("Please, write a positive time.")
        except ValueError:
            print("Please, write a correct time value.")

def query():
    while True:
        try: 
            print("Do you need another query? Y/n.")
            ans = input()
            if ans in ['Y', 'y', 'Yes', 'yes']:
                return True
            elif ans in ['N', 'n', 'No', 'no']:
                return False
            else:
                print('Please, try again,')
        except Exception as e:
            print('An error has occurried:', e)


def main_caigudallure():
    y0, v0 = entrada()

    while True:
        opt = options()

        if opt == 1:
            see_eq_mov(y0, v0)
        elif opt == 2:
            t = time()
            print(pos_in_time(y0, v0, t))
        elif opt == 3:
            see_eq_vel(v0)
        elif opt == 4:
            t = time()
            print(vel_in_time(v0, t))
        elif opt == 5:
            t = time()
            grafica(y0, v0, t)
        elif opt == 6:
            print(max_hight(y0, v0))
        elif opt == 7:
            print(tiempo_caer(y0, v0))
                
        if not query():
            print("Finishing this movement.")
            return



