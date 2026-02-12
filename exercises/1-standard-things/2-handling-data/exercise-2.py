#!/bin/python3

# Objective:
## Using the values array below, run the following steps in order.
##
## Delete the last item
## Set the second element to the number 8
## Flip the array
## Append the numbers 5 and 9 to the array
## Print out the array

###### Given variables ######
values = [1, 2, 3, 4, 5]
#############################

## Delete the last item
del values[-1]
## Set the second element to the number 8
values[1] = 8
## Flip the array
values = values[::-1]
## Append the numbers 5 and 9 to the array
values.append(5)
values.append(9)
## Print out the array
print(values)
