#!/bin/python3

import pandas as pd

# You are part of a team working on analyzing planetary Earth data. Your task is to process and analyze the data using Pandas to extract insights.
# Objectives:
##     Create a Pandas Series representing distances of planets from the Sun (in million kilometers)
##     Create a Pandas DataFrame representing characteristics of moons of the outer planets
##     Analyze the data to find key information about planetary distances and moon characteristics

###### Given variables ######
planet_distances = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.6,
    "Saturn": 1433.5,
    "Uranus": 2872.5,
    "Neptune": 4495.1,
    "Pluto": 5906.4,
}

moon_data = {
    "Planet": ["Jupiter", "Jupiter", "Saturn", "Saturn", "Uranus", "Neptune"],
    "Moon": ["Io", "Ganymede", "Titan", "Rhea", "Titania", "Triton"],
    "Diameter (km)": [3642, 5262, 5150, 1528, 1578, 2707],
    "Orbital Period (days)": [1.77, 7.15, 15.95, 4.52, 8.71, 5.88],
}
#############################

planet_distances_from_sun = pd.Series(planet_distances)
moon_characteristics = pd.DataFrame(moon_data)

print(f"Average distance of planets from the Sun: {planet_distances_from_sun.mean()}\n")

## this gives a list of planets with moons without duplicate planet names
planets_with_moons = list(set(moon_data["Planet"]))

print("Number of moons each planet have:")
for planet in planets_with_moons:
    number_of_moons = len(
        moon_characteristics[moon_characteristics["Planet"] == planet]["Moon"]
    )
    print(f"- {planet}: {number_of_moons} moons")

print("\nLargest moon of each planet:")
for planet in planets_with_moons:
    largest_moon = (
        moon_characteristics[moon_characteristics["Planet"] == planet]
        .sort_values(by="Diameter (km)", ascending=False)
        .iloc[0]
    )
    print(f"- {planet}: {largest_moon['Moon']}, {largest_moon['Diameter (km)']} km")
