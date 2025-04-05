# Newton's second law: F = ma
# Coulomb friction force: Ff = uN, where N = m*g
#Assumption of units: mass in kg, velocity in m/s, acceleration in m/s^2

import plotly
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


#Constants
# g = 9.81
# m = 1 # mass
# # u = 0.3 #coefficient of friction
# # v0 = 10  # initial velocity
# ts = 0.01 # time step
# N = m * g



def simulate_motion(v0, u, g):

    #initial conditions
    x = 0.0
    t = 0.0
    t_max = 5
    v = v0
    m = 1.0
    ts = 0.01

    #Arrays to plot variables
    times = []
    distances = []
    velocities = []

    while abs(v) > 1e-5 and t <= t_max:
        friction_force = -np.sign(v) * u * m * g
        acc = friction_force / m


        v += acc * ts
        x += v * ts
        t += ts
        times.append(t)
        distances.append(x)
        velocities.append(v)

    print("Simulation complete.")
    print(f"Final position: {x:.2f} m")
    print(f"Final velocity: {v:.5f} m/s")
    print(f"Total time simulated: {t:.2f} s")

    # return times, distances, velocities

    fig = px.line(x=times, y=distances)
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(
    #     x=distances,
    #     y=velocities,
    #     mode='lines',
    #     name='Line'
    # ))
    fig.update_layout(
        title='Position vs. Time',
        yaxis_title='Position (m)',
        xaxis_title='Time (s)',
        showlegend=True,
        # xaxis_range=[0,2]
    #
     )
    fig.show()

def main():
    v0 = float(input("Enter the initial velocity of the object in m/s. "))
    u = float(input("Enter the coefficient of friction (must be between 0 and 1) "))
    g = float(input("Enter the value of acceleration due to gravity. "))  # must be 9.81

    print(f"Using μ={u}, v0={v0}, g={g}")
    simulate_motion(v0, u, g)

if __name__ == "__main__":
    main()