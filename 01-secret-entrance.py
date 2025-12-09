# README ------------------------------------------------------------------------------------------
# 
#   file: 01-secret-entrance.py
#   desc: day 1 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/1
# 
# -------------------------------------------------------------------------------------------------

# packages ----------------------------------------------------------------------------------------

import argparse 
import time

# prepare data ------------------------------------------------------------------------------------

print("\nStarting Script") 
print("---" * 40)
start_time = time.time()

## define script arguments 
parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to txt file of lock rotations")
args = parser.parse_args() 

## read in rotations
with open(args.data, "r") as file: 
    rotations = file.readlines()

rotations = [r.replace("\n", "") for r in rotations]


# perform rotations -------------------------------------------------------------------------------

## convert each rotation to numeric (left = negative, right = positive) 
directions = [r[0] for r in rotations] 
magnitudes = [int(r[1:]) for r in rotations] 

numeric_rotations = []
for d, m in zip(directions, magnitudes): 
    if (d == "L"): 
        m = -m
    numeric_rotations.append(m) 

## iterate over rotations with puzzle #1 logic (landing on zero increases counter by 1)
zero_counter = 0 
position = 50 

for r in numeric_rotations: 
    position += r
    if (position > 99) or (position < 0): 
        position = position % 100 
    if (position == 0): 
        zero_counter += 1 

print(f"Puzzle #1: {zero_counter}")

## iterate over rotations with puzzle #2 logic (passing over 0 increases counter by 1) 
zero_counter = 0 
position = 50 

just_passed = False
for r in numeric_rotations: 

    ## reduce rotation to scale of -99 to 99
    while (r > 100): 
        r -= 100 
        zero_counter += 1
    while (r < -100): 
        r += 100 
        zero_counter += 1
    
    ## apply final rotation
    end = position + r 
    
    ## update zero counter + rotation if passing zero
    if (end == 0): 
        zero_counter += 1
    elif (end >= 100): 
        zero_counter += 1
        end = end % 100 
    elif (end < 0): 
        if (position != 0): 
            zero_counter += 1 
        end = end % 100 

    position = end

print(f"Puzzle #2: {zero_counter}")

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")