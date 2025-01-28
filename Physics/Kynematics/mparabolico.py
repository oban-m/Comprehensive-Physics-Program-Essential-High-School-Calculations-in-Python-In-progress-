"""
    PROGRAMA PEL MOVIMENT PARABOLIC
"""

import math
import matplotlib.pyplot as plt

g = -9.807

def opcio():
    while True:
        try:
            print("Options: "
                "1) Equations of the positions."
                "2) Position in a specific time."
                "3) Equation of the velocitities."
                "4) Velocity vector and modul velocitz in a specific time."
                "5) Maximun height"
                "6) Time to reach ground (if initial hight is zero)."
                "7) Maximum reach."
                "8) Plot of the movement x-y."
                )
            opt = int(input())
            if opt in [1, 2, 3, 4, 5, 6, 7, 8]:
                return opt
            else:
                print("Please, try again.")
        except ValueError:
            print("Please, try again.")
        
            
def entrada():
    while True:
        try:
            print("Write the initial point in x axis:")
            x = float(input())
            print("Write the initial point in y axis:")
            y = float(input())
            print("Write the module of the initial velocity.")
            v0 = float(input())
            print("Write the angle that mass if thrown, in grades.")
            theta = float(input())
            return x, y, v0, theta
        except ValueError:
            print("Please, try again.")

def vel_descom(v0, theta):
    return v0 * math.cos(theta * (math.pi / 180)), v0 * math.sin(theta * (math.pi / 180))

def see_eq_movement(x0, y0, v0, theta):
    global g

    v0x, v0y = vel_descom(v0, theta)
    print(f"Axis x: x(t) = {x0} + {v0x} * t")
    print(f"Axis y: y(t) = {y0} + {v0y} * t  {(1/2) * g} * t ** 2")
    pass

def see_eq_velocity(v0, theta):
    global g

    v0x, v0y = vel_descom(v0, theta)
    print(f"Axis x: v_x(t) = {v0x}")
    print(f"Axis y: v_y(t) = {v0y} {g} * t")
    pass

def position_in_time(x0, y0, v0, theta, t):
    global g

    v0x, v0y = vel_descom(v0, theta)
    return x0 + v0x * t, y0 + v0y * t +  0.5 * g * (t**2)  

def velocity_in_time(v0, theta, t):
    global g

    v0x, v0y = vel_descom(v0, theta)
    return v0x, v0y + g * t, math.sqrt((v0x) ** 2 + (v0y + g * t) ** 2)

def max_height(y0, v0, theta):
    global g

    if y0 == 0:
        v0x, v0y = vel_descom(v0, theta)
        return v0y ** 2 / (2 * abs(g))
    else:
        print("Initial height must be zero.")
        pass

def max_time(y0, v0, tetha):
    global g

    if y0 == 0:
        v0x, v0y = vel_descom(v0, tetha)
        return (2 * v0y) / abs(g)
    
def max_x(x0, y0, v0, theta):
    global g

    if x0 == 0 and y0 == 0:
        return (v0 ** 2 * math.sin(2 * theta * (math.pi / 180))) / abs(g)
    elif y0 == 0:
        return x0 + (v0 ** 2 * math.sin(2 * theta * (math.pi / 180))) / abs(g)
    else:
        print("Can not be calculated, initial y point must be zero.")
        pass

def tim():
    while True:
        try:
            print("Write a specific time.")
            time = float(input())
            if time >= 0:
                return time
            
            print("Time must be positive or zero, try again.")
        except ValueError:
            print("Write a correct value of time, please.")

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

def main_parabolico():
    x0, y0, v0, theta = entrada()
    
    while True:
        opt = opcio()

        if opt == 1:
            see_eq_movement(x0, y0, v0, theta)
        elif opt == 2:
            t = tim()
            X_x, Y_y =position_in_time(x0, y0, v0, theta, t)
            print(f"Position in axis x: {X_x}, Position in axis y: {Y_y}")
        elif opt == 3:
            see_eq_velocity(v0, theta)
        elif opt == 4:
            t = tim()
            vx, vy, v = velocity_in_time(v0, theta, t)
            print(f"Velocity axis x: {vx}, Velocity axis y: {vy}, Module Velocity: {v}")
        elif opt == 5:
            print(max_height(y0, v0, theta))
        elif opt == 6:
            print(max_time(y0, v0, theta))
        elif opt == 7:
            print(max_x(x0, y0, v0, theta))
        elif opt == 8:
            print("Devolvoing")

        if not query():
            print("Finishing this movement.")
            return 
