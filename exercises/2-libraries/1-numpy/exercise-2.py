#!/bin/python3

# Objectives:
## Use NumPy's random number generation functions to generate simulated altitude, velocity, and acceleration data.
## Assume that the flight data consists of 1000 data points each for altitude, velocity, and acceleration.
## Perform array indexing and slicing to extract subsets of data for analysis.
## Use array comparisons and conditional methods to identify critical points:
#### Critical altitude: Altitude above 5000 meters.
#### Critical velocity: Velocity greater than 300 meters per second.
#### Critical acceleration: Acceleration less than -9.8 meters per second squared (indicating deceleration).
## Concatenate arrays representing critical points to an array and print it out!

import numpy as np

altitude = np.random.uniform(0, 1000, 1000)
## Bigger than mach 1 - 295 m/s
velocity = np.random.uniform(0, 350, 1000)
## I decided to generate between -30, 30
acceleration = np.random.uniform(-30, 30, 1000)

critical_altitude = altitude[altitude > 5000]
critical_velocity = velocity[velocity > 300]
critical_acceleration = acceleration[acceleration < -9.8]

critical_values = np.concatenate(
    (critical_altitude, critical_velocity, critical_acceleration)
)

print(critical_values)
