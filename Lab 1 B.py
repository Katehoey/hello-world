# Grace Rapisarda and Kate Hoey

# Loyola University Maryland
# Thursday Jan 28
# Lab 1

import math

# output purpose
print("The purpose of this program is to ask user for mL and convert mL to tsp and tbsp")

# ask user for the input mL

mL = input("Please enter the number of mL: ")
mL = float(mL)

# equation for mL to tsp

teaspoons = mL/5

# compute the teaspoons

print("The number of teaspoons is: ", teaspoons)

# equation for tablespoons

tablespoons = teaspoons/3

# compute the tablespoons

print("The number of tablespoons is: ", tablespoons)
