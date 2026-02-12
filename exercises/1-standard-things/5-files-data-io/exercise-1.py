#!/bin/python3

# You are a planetary scientist tasked with saving orbital details about planets into a file for later use
# Objective:
## Initialize a text file named orbital_details
## Iterate over all the planets and save their orbital details into the text file

###### Given variables ######
planet_names = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]

# Orbital periods (in Earth years)
orbital_periods = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]

# Axial tilts (in degrees)
axial_tilts = [0.03, 177.36, 23.44, 25.19, 3.13, 26.73, 82.23, 28.32]
#############################

file = open("orbital_details", "w")

for index, planet_name in enumerate(planet_names):
    file.write(
        f"{planet_name}, period: {orbital_periods[index]} Earth Years, axial tilt: {axial_tilts[index]} Degrees\n"
    )

file.close()
