#!/bin/python3

# Create multiple variables and print out all of them

import random

astronaut_name = "Zod"
astronaut_age = "24"

fuel = round(random.uniform(30.0, 53.0), 2)
is_engine_running = True

astronauts = ["Zod", "Ed", "Paul"]
astronaut_ages = {"Zod": 24, "Ed": 30, "Paul": 38}

# Astronaut information
print("--- Astronaut Information ---")
print(f"Astronaut Name: {astronaut_name}\nAstronaut Age: {astronaut_age}")

# Fuel/Engine information
print("--- Fuel/Engine Information ---")
print(f"Fuel: {fuel}\nIs Engine Running: {is_engine_running}")

# Information of all atronauts
print("--- Information of all atronauts ---")
print(f"Astronauts: {astronauts}\nAstronaut Ages: {astronaut_ages}")
