# Newton's second law: F = ma, a = F/m
# Coulomb friction force: Ff = uN, where u is friction coefficient and N = m*g
# Assumption of units: mass in kg, velocity in m/s, gravitational acceleration is always 9.81 m/s^2

# import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
# import pandas as pd
# import logging


def simulate_motion(v0, u, g):
    """
    Simulate motion of an object subjected to coulomb friction moving horizontally on a surface.

    This function prompts the user to input 3 values: initial velocity,
    coefficient of friction, and acceleration due to gravity in order to
    calculate distance/velocity/acceleration of object until coming to
    a complete stop.

    Args:
        v0 (int or float): the initial velocity.
        u (float between 0 and 1): coefficient of friction
        g (float): gravitational acceleration, must be 9.81 m/s^2

    Returns:
        None, but outputs visualization of velocity and positions.
    """
    #Initial conditions
    x = 0.0       # position (m)
    t = 0.0       # time (s)
    t_max = 5     # max time interval (s)
    v = v0        # initial velocity (m/s)
    m = 1.0       # mass (kg)
    ts = 0.01     # time-step (s)

    #Lists to store values for plotting
    times = []
    distances = []
    velocities = []

    while abs(v) > 1e-5 and t <= t_max:
        friction_force = -np.sign(v) * u * m * g
        acc = friction_force / m # also acc = -u*g

        #Check for overshoot - changes direction
        new_v = v + acc * ts
        if np.sign(new_v) != np.sign(v):
            v = 0.0
            break
        else: # if direction isn't changing, continue updating values and adding to list
            v += acc * ts
            x += v * ts
            t += ts
            times.append(t)
            distances.append(x)
            velocities.append(v)

    #Final values of x, v, t
    print("Simulation complete.")
    print(f"Final position: {x:.2f} m")
    print(f"Final velocity: {v:.2f} m/s")
    print(f"Total time simulated: {t:.2f} s")


    # For improving app: return times, distances, velocities to be used for testing/analysis.


    #Visualization using Plotly

    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=("Position vs. Time", "Velocity vs. Time")
                        )

    fig.add_trace(go.Scatter(
        x=times,
        y=distances,
        showlegend=False
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=times,
        y=velocities,
        showlegend=False
    ), row=2, col=1)

    fig.update_xaxes(title_text="Time (s)", row=1, col=1)
    fig.update_xaxes(title_text="Time (s)", row=2, col=1)

    fig.update_yaxes(title_text="Position (m)", row=1, col=1)
    fig.update_yaxes(title_text="Velocity (m/s)", row=2, col=1)

    fig.update_layout(title="Motion Under Coulomb Friction", height=750, width=1350)

    fig.show()

#Validation for inputs
def validate_v0(value):
    try:
        value = float(value)
    except ValueError:
        raise ValueError("Initial velocity must be a number.")
    if value <= 0:
        raise ValueError("Initial velocity must be greater than 0.")
    return value

def get_valid_v0():
    while True:
        try:
            user_input = input("Enter the initial velocity of the object in m/s: ")
            return validate_v0(user_input)
        except ValueError as e:
            print(f"Error: {e} ")


def validate_u(value):
    try:
        value = float(value)
    except ValueError:
        print("Coefficient must be a number.")
    if value < 0 or value > 1:
        raise ValueError("Coefficient of friction must be between 0 and 1. ")
    return value

def get_valid_u():
    while True:
        try:
            user_input = input("Enter the coefficient of friction. ")
            return validate_u(user_input)
        except ValueError as e:
            print(f"Error: {e}")

def validate_g(value):
    try:
        value = float(value)
    except ValueError:
        print("Acceleration must be a number.")
    if not value == 9.81:
        raise ValueError("Gravitational acceleration must be 9.81")
    return value

def get_valid_g():
    while True:
        try:
            user_input = input("Enter the value of acceleration due to gravity. ")
            return validate_g(user_input)
        except ValueError as e:
            print(f"Error: {e} ")


def main():

    v0 = get_valid_v0()
    u = get_valid_u()
    g = get_valid_g()


    print(f"Using μ={u}, v0={v0}, g={g}")
    simulate_motion(v0, u, g)

if __name__ == "__main__":
    main()