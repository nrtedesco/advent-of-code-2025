# README ------------------------------------------------------------------------------------------
# 
#   file: 01-secret-entrance.py
#   desc: code for first challenge of Advent of Code 2025 
# 
# -------------------------------------------------------------------------------------------------

# packages ----------------------------------------------------------------------------------------

import argparse 

# prepare data ------------------------------------------------------------------------------------

## define script arguments 
parser = argparse.ArgumentParser() 
parser.add_argument("-c", "--config", help="path to txt file of lock rotations")
args = parser.parse_args() 

## read in rotations
with open(args.config, "r") as file: 
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

just_swapped = False
for r in numeric_rotations: 
    if (position == 0) and (just_swapped) and (r < 0): 
        zero_counter -= 1
    position += r
    just_swapped = False
    while (position < 0): 
        position += 100 
        zero_counter += 1
        just_swapped = True
    while (position > 99): 
        position -= 100 
        zero_counter += 1 
        just_swapped = True

print(f"Puzzle #2: {zero_counter}")