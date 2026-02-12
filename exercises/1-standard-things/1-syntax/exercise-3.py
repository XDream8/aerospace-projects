#!/bin/python3

# Task: Do basic space resource calculations, Purpose: Learn basic math operations in python
## Calculate and print the total distance traveled
## Calculate and print the total fuel consumed
## Calculate and print the total time to destination
## Create a variable called full_name and print out the full name of the astronaut

###### Given variables ######
travel_time = 10  # hours
speed = 5000  # kilometers per hour
fuel_efficiency = 10  # kilometers per liter
first_name = "Sally"
last_name = "Ride"
#############################

## total distance traveled
## Distance = Speed x Time
distance = speed * travel_time
print(f"Total Distance Traveled: {distance}")

## total fuel consumed
## Fuel Consumption = Distance / Fuel Efficiency
fuel_consumption = distance / fuel_efficiency
print(f"Fuel Consumption: {fuel_consumption}")

## time to destination
## Time to Destination = Distance / Speed
time_to_destination = distance / speed
print(f"Time to Destination: {time_to_destination}")

## full name
full_name = f"{first_name} {last_name}"
print(f"Full Name: {full_name}")
