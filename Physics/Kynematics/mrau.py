"""
    PROGRAMA PEL MOVIMENT MRUA GENERAL I MRU EN CAS QUE a = 0.
"""


import matplotlib.pyplot as plt
import math

def entrada():
    while True:
        try:
            print("Write the inicial point of the mass in meters:")
            x0 = float(input())
            print('Write the inicial velocity of the mass in meters:')
            v0 = float(input())
            print("Write the acceleration of the mass:")
            a = float(input())
            return x0, v0, a
        except ValueError:
            print('Write correct values.')

def opcio():
    while True:
        try:
            print("Options: 1) Equation of movement. 2) Position in future time. 3) Equation of velocity. 4) Velocity in future time. 5) Show plot in time: Position&Velocity/Time." )
            opt = int(input())
            if opt in [1, 2, 3, 4, 5]:
                return opt
            else:
                print('Write a correct value.')
        except ValueError:
            print("Write an integer from 1 to 4, please.")

def time():
    while True:
        try:
            print('Write the time which you want to know the position')
            time = float(input())
            if time >= 0:
                return time
            print('Write a positive time.')
        except ValueError:
            print('Write a correct value.')

def query():
    while True:
        try: 
            print('Do you want to do another query? Y/n.')
            answer = input()
            if answer in ['Y', 'y', 'yes', 'Yes']:
                return True
            elif answer in ['N', 'n', 'No', 'no']:
                return False
            else:
                print("Please write a correct answer.")
        except Exception as e:
            print('An error has ocurried:', e)



def see_eq_mov(x0, v0, a):
    print("The equation of the movement for this mass is:")
    print(f"x(t) = {x0} + {v0} * t + 1/2 * {a} * t ** 2")
    pass

def see_eq_vel(v0, a):
    print('The equation of the velocity for this mass is:')
    print(f"v(t) = {v0} + {a} * t")
    pass

def pos_in_time(x0, v0, a, t):
    return x0 + v0 * t + 1/2 * a * t ** 2

def vel_in_time(v0, a, t):
    return v0 + a * t

def grafica(x0, v0, a, t): 
    times = [_ for _ in range(0, math.ceil(t)+1)]
    positions = list(map(lambda time: pos_in_time(x0, v0, a, time), times))
    velocities = list(map(lambda time: vel_in_time(v0, a, time), times))

    plt.figure()
    plt.plot(times, positions, label = 'Position / Time', color = 'blue')
    plt.plot(times, velocities, label = 'Velocity / Time', color = 'red')
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Position - Velocity')
    plt.title('Position & Velocity / Time')
    plt.legend()
    plt.grid(True)
    plt.show()
    pass
            
def main_mrua():
    x0, v0, a = entrada()
    while True:
        option = opcio()
        if option == 1:
            see_eq_mov(x0, v0, a)
        elif option == 2:
            t = time()
            print(pos_in_time(x0, v0, a, t))
        elif option == 3:
            see_eq_vel(v0, a)
        elif option == 4:
            t = time()
            print(vel_in_time(v0, a, t))
        elif option == 5:
            t = time()
            grafica(x0, v0, a, t)

        ans = query()
        if not ans:
            break
    print("Finishing this movement.")
    return 
