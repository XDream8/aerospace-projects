#!/bin/python3

# Objective:
## Calculator must ask the user for the thrust and mass flow rate of the propellant
## Typecast the values as float variables
## Calculate the specific impulse of the rocket engine
## Calculate the exhaust velocity of the rocket
## Print out the values as strings

## HINT: you can use the below equations
## Specific Impulse = Thrust / (Mass Flow Rate * 9.81)
## Exhaust Velocity = Specific Impulse * 9.81

thrust = float(input("Thrust: "))
mass_flow_rate = float(input("Mass flow rate of the propellant: "))

specific_impulse = thrust / (mass_flow_rate * 9.81)
exhaust_velocity = specific_impulse * 9.81

print(f"Specific Impulse: {specific_impulse}")
print(f"Exhaust Velocity: {exhaust_velocity}")
