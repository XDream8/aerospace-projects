#!/bin/python3

# Objective:
## Typecast fuel_remaining (float) into an int
## Typecast oxygen_levels (int) into a float
## Print out the outputs to look like the following:
##   Fuel Remaining: 33 L
##   Oxygen Levels: 21.0 kPa

###### Given variables ######
fuel_remaining = 33.42
oxygen_levels = 21
#############################

## typecasting
fuel_remaining = int(fuel_remaining)
oxygen_levels = float(oxygen_levels)

## print out
print(f"Fuel Remaining: {fuel_remaining} L")
print(f"Oxygen Levels: {oxygen_levels} kPa")
