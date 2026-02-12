#!/bin/python3

# Write a calculator using the math module that contains the following features:
# Objective:
## Write a function called pow that takes inputs a and b and returns the power
## Write a function called ceiling that takes input a returns math.ceil
## Write a function called floor that takes input a returns math.floor
## Write a function called factorial that takes input a returns math.factorial
## Use the variables a and b as needed for each function

import math

###### Given variables ######
a = 4
b = 5
#############################


## Write a function called pow that takes inputs a and b and returns the power
def pow(a, b):
    return math.pow(a, b)


## Write a function called ceiling that takes input a returns math.ceil
def ceiling(a):
    return math.ceil(a)


## Write a function called floor that takes input a returns math.floor
def floor(a):
    return math.floor(a)


## Write a function called factorial that takes input a returns math.factorial
def factorial(a):
    return math.factorial(a)


## Use the variables a and b for each function
print(f"pow: {pow(a, b)}")
print(f"ceiling: {ceiling(a)}")
print(f"floor: {floor(a)}")
print(f"factorial: {factorial(a)}")
