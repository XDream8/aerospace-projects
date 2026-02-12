#!/bin/python3

# You are tasked with creating a simple Python program to simulate space mission control operations. The program should incorporate various control flow structures to manage different aspects of the mission.
# Objective:
## Initialize a while loop that runs when the mission time is less than or equal to the mission duration
## Within the while loop, decrease the distance to the destination by the distance traveled per hour
## Within the while loop, decrease the fuel level by the fuel consumption rate
## Within the while loop, print out the fuel level, mission time, distance to destination
## Break out the while loop if fuel level OR distance to the destination is less than or equal to 0
## Increment the mission time by one after each time

###### Given variables ######
mission_duration = 10  # Duration of the mission in hours
fuel_level = 1000  # Initial fuel level in gallons
distance_to_destination = 500000  # Distance to the destination in kilometers
mission_time = 0  # Initialize mission time
fuel_consumption_rate = 50  # gallons per hour
distance_traveled_per_hour = 50000  # kilometers per hour
#############################

while mission_time <= mission_duration:
    distance_to_destination -= distance_traveled_per_hour
    fuel_level -= fuel_consumption_rate
    print(
        f"Mission Time: {mission_time} hours, Fuel Level: {fuel_level} gallons, Distance to Destination: {distance_to_destination} kilometers"
    )
    if fuel_level <= 0 or distance_to_destination <= 0:
        break
    mission_time += 1
