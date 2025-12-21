# README ------------------------------------------------------------------------------------------
# 
#   file: 07-laboratories.py
#   desc: day 7 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/7
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time 

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    beam_data = file.readlines()
    beam_data = [row.replace('\n', '') for row in beam_data]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)

## determine beam start position 
beam_start = 0 
while (beam_data[0][beam_start] != "S"): 
    beam_start += 1


# part 1 ------------------------------------------------------------------------------------------

## iterate over rows, keeping track of current beam positions + split counter 

beam_positions = set([beam_start]) 
split_counter = 0 

for row in beam_data[1:]: 
    new_beam_positions = set() 
    for i in beam_positions: 
        if (row[i] == "^"): 
            new_beam_positions.add(i-1)   # add split left 
            new_beam_positions.add(i+1)   # add split right 
            split_counter += 1
        else: 
            new_beam_positions.add(i) 
    beam_positions = new_beam_positions 

print(f"Puzzle #1: {split_counter}")


# part 2 ------------------------------------------------------------------------------------------

## define recursive function to search each path to bottom of tree

global explored
explored = {} 

def search_paths(position:int, row:int, beam_data:list[str]) -> int: 
    
    ## base case: reached end of beam data 
    if (row == len(beam_data)): 
        return 1
    
    ## recursive call: determine if position results in split, or continues w/o split 
    next_row = row + 1
    if (beam_data[row][position] == "^"): 
        
        # search left 
        left_position = position - 1
        left_key = f"{left_position} {next_row}"
        if (left_key in explored.keys()): 
            left_val = explored[left_key] 
        else: 
            left_val = search_paths(left_position, next_row, beam_data) 
            explored[left_key] = left_val 

        # search right 
        right_position = position + 1
        right_key = f"{right_position} {next_row}"
        if (right_key in explored.keys()): 
            right_val = explored[right_key] 
        else: 
            right_val = search_paths(right_position, next_row, beam_data) 
            explored[right_key] = right_val 

        return left_val + right_val 
    
    else: 

        down_key = f"{position} {next_row}"
        if (down_key in explored.keys()): 
            down_val = explored[down_key]
        else: 
            down_val = search_paths(position, next_row, beam_data)
            explored[down_key] = down_val 

        return down_val 

## start search with initial beam position 
path_counter = search_paths(beam_start, 1, beam_data) 

print(f"Puzzle #2: {path_counter}")
    

# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")