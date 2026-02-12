#!/bin/python3

# You are an astronomer recruited to analyze the luminosity of celestial objects in the night sky.
# Objective:
## Print out all the names of the celestial bodies using a for loop
## Initialize an array variable to contain only the luminosities of the solar objects
## Iterate over the luminosities using a while loop AND use a conditional print out all the celestial bodies with a luminosity of less than 200 solar units

## HINT: you can iterate over an object celestial_objects like the following:
## for obj in celestial_objects.items():
##     print(obj[0] + ":", obj[1], "solar units")

###### Given variables ######
celestial_objects = {
    "Sirius": 25,  # Sirius is one of the brightest stars in the night sky
    "Andromeda Galaxy": 1000000,  # Andromeda Galaxy has a very high luminosity
    "Jupiter": 0.00006,  # Jupiter reflects sunlight but has low intrinsic luminosity
    "Pleiades": 100,  # The Pleiades star cluster is moderately luminous
    "Orion Nebula": 10000,  # The Orion Nebula is a bright emission nebula
}
#############################


## Print out all the names of the celestial bodies using a for loop
for obj in celestial_objects.items():
    print(obj[0])

## Initialize an array variable to contain only the luminosities of the solar objects
luminosities = []
for obj in celestial_objects.items():
    luminosities.append(obj[1])

## Iterate over the luminosities using a while loop AND use a conditional print out all the celestial bodies with a luminosity of less than 200 solar units
i = 0
while i < len(luminosities):
    luminosity = luminosities[i]
    if luminosity < 200:
        print(luminosity)
    i += 1
