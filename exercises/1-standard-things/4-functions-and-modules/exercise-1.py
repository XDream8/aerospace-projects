#!/bin/python3

# You are tasked with creating a calculator program with the following specifications:
# Objective:
## Create a function called add that takes in two numbers and returns the sum
## Create a function called subtract that takes in two numbers and returns the difference
## Create a function called divide that takes in two numbers and returns the divided output
## Create a function called multiply that takes in two numbers and returns the multiplied output
## Create test values for all the functions and print them out!
## Utilize variables a and b for testing

###### Given variables ######
a = 4
b = 5
#############################


## Create a function called add that takes in two numbers and returns the sum
def add(a, b):
    return a + b


## Create a function called subtract that takes in two numbers and returns the difference
def subtract(a, b):
    return a - b


## Create a function called divide that takes in two numbers and returns the divided output
def divide(a, b):
    return a / b


## Create a function called multiply that takes in two numbers and returns the multiplied output
def multiply(a, b):
    return a * b


## Utilize variables a and b for testing
print(
    f"Add: {add(a, b)}, Subtract: {subtract(a, b)}, Divide: {divide(a, b)}, Multiply: {multiply(a, b)}",
)
