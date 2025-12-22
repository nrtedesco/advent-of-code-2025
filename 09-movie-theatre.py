# README ------------------------------------------------------------------------------------------
# 
#   file: 09-movie-theatre.py
#   desc: day 9 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/9
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time
import csv  
import numpy as np

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
parser.add_argument("-n", "--n_connections", help="total number of connections for puzzle 1")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    floor = [r for r in csv.reader(file)]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)

floor = np.array(floor).astype(int)


# part 1 ------------------------------------------------------------------------------------------

## compute area for each tile pair, keeping track of max

max_area = -1
for i in range(len(floor)): 
    for j in range(i+1, len(floor)): 
        curr_area = np.prod(np.abs(floor[i] - floor[j]) + 1)       # must add 1 since rectangle is inclusive of bounds
        if (curr_area > max_area): 
            max_area = curr_area 

print(f"Puzzle #1: {max_area}")


# part 2 ------------------------------------------------------------------------------------------



# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")