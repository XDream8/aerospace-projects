#!/bin/python3

# You are part of a team developing a flight trajectory planning software for a space mission to Mars. The software requires efficient handling of numerical data for trajectory calculations and simulations.
# Objectives:
## Generate a NumPy array representing time in seconds from t=0 to t=100 seconds with a step size of 1 second.
## Generate a NumPy array representing altitude in meters during the launch phase. The altitude should start at 0 meters and increase linearly with time at a constant rate of 100 meters per second.
## Calculate the velocity array using the altitude array. Assume constant acceleration due to gravity (9.81 m/s^2) during the launch phase.
## Calculate the acceleration array using a constant acceleration value of 9.81 m/s^2.
## Print the shape and data type of each generated NumPy array

import numpy as np

###### Given variables ######
gravity_acceleration = 9.81  # Constant acceleration due to gravity in m/s^2
#############################

## Generate a NumPy array representing time in seconds from t=0 to t=100 seconds with a step size of 1 second.
time = np.arange(0, 101, 1)

## Generate a NumPy array representing altitude in meters during the launch phase. The altitude should start at 0 meters and increase linearly with time at a constant rate of 100 meters per second.
altitude = np.linspace(0, 100 * 100, 100 + 1)

## Calculate the velocity array using the altitude array. Assume constant acceleration due to gravity (9.81 m/s^2) during the launch phase.
## V = sqrt(2 * a * h)
velocity = gravity_acceleration * time

## Calculate the acceleration array using a constant acceleration value of 9.81 m/s^2.
acceleration = np.full(time.shape, gravity_acceleration)

## Print the shape and data type of each generated NumPy array
print(f"Time array, shape: {time.shape}, data type: {time.dtype}")
print(f"Altitude array, shape: {altitude.shape}, data type: {altitude.dtype}")
print(f"Velocity array, shape: {velocity.shape}, data type: {velocity.dtype}")
print(
    f"Acceleration array, shape: {acceleration.shape}, data type: {acceleration.dtype}"
)
