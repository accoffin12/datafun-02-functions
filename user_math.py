"""
Always start with a docstring that describes what the module does.
Include your name and the date.

Alexandra Coffin
Data Analysis Fundementals Project 2
Janurary 22, 2023
Project Goal: to write custom function using exclusions and tunctions from math mod.

"""

import math
import time

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?
    
    Yes if 0, a negative number or character is entered. 

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
"""Defines Cost of Car Essentials for total year"""
def cost_of_car(cost_of_engines, engines, cost_power_unit, power_units):
    try:    
        annual_drive_train = cost_of_engines * engines
        annual_power_unit = cost_power_unit * power_units
        cost_of_car = math.fsum([annual_drive_train + annual_power_unit])
        return cost_of_car
    except Exception as ex:
        print(f"Error: {ex}")
        return None
#-----------------------------------------------------------------------------------------------------------
"""Returns Miles Driven per Year by 1 car."""
def total_race(laps, track_length, races, qualifying):
    race_miles = (laps * track_length)
    total_race = math.fsum([race_miles + qualifying])
    return total_race
#------------------------------------------------------------------------------------------------------------
"""Returns the range of a set of laptimes"""
# 
def range_lap_times(highest, lowest):
    range = highest - lowest
    return range

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print(f"get_total_area_of_lot(6, 2) = {get_area_of_lot(6, 2)}")
    print(f"cost_of_car(2450, 3, 4610, 4) = {cost_of_car(6750, 3, 4500, 4)}")
    print(f"total_race(246, 198.194, 22) = {total_race(246, 199, 22, 15692)}")
    print(f"range_lap_times in miliseconds(26, 15, 49) = {range(26, 15, 49)}")