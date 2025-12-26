# README ------------------------------------------------------------------------------------------
# 
#   file: 09-movie-theatre.py
#   desc: day 9 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/9
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time
import numpy as np

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
parser.add_argument("-n", "--n_connections", help="total number of connections for puzzle 1")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    manual = file.readlines() 
    manual = [r.replace('\n', '') for r in manual]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)


# part 1 ------------------------------------------------------------------------------------------

## strategy: use BFS to extend search one button press at a time. break when solution is found 

# button_presses = 0 
# for machine in manual: 
#     # parse machine components (indicator lights + buttons) from line 
#     desired_config  = machine.replace('[', '').replace(']', '').split()[0]
#     raw_buttons = machine.split(']')[1].split('{')[0].replace('(', '').replace(')', '').split()
#     buttons = []
#     for button in raw_buttons: 
#         buttons.append([int(v) for v in button.split(',')])

#     # check edge case - starting position is desired position 
#     start_config = ['.'] * len(desired_config)
#     if (start_config == desired_config): 
#         continue 

#     # start BFS
#     i = 0 
#     paths = [start_config]
#     solved = False

#     while (not solved): 
#         i += 1
#         next_paths = [] 
#         for path in paths: 
#             for button in buttons: 
#                 next_path = path[:]
#                 for num in button: 
#                     if (next_path[num] == '#'): 
#                         next_path[num] = '.'
#                     else: 
#                         next_path[num] = '#'
#                 if (''.join(next_path) == desired_config): 
#                     solved = True 
#                     break 
#                 next_paths.append(next_path) 
#             if (solved): 
#                 break 
#         paths = next_paths 
    
#     button_presses += i 

# print(f"Puzzle 1: {button_presses}")


# puzzle 2 ----------------------------------------------------------------------------------------

## strategy: use BFS to extend search one button press at a time, but now search relative to joltage requirements 

def check_joltage(curr_joltage:list[int], min_joltage:list[int]) -> bool: 

    satisfied = True
    for v1, v2 in zip(curr_joltage, min_joltage): 
        if (v1 < v2): 
            satisfied = False 

    return satisfied 


button_presses = 0 
for machine in manual: 
    # parse machine components (required joltage + buttons) from line 
    min_joltage = np.array([int(v) for v in machine.split('{')[1].replace('}', '').split(',')])
    buttons = [np.array([int(v) for v in b.split(',')]) for b in machine.split(']')[1].split('{')[0].replace('(', '').replace(')', '').split()]

    # set default joltage + check against requirements 
    start_joltage = [0] * len(min_joltage)
    if (check_joltage(start_joltage, min_joltage)): 
        continue 

    # start search 
    i = 0 
    solved = False 
    paths = [start_joltage] 
    visited = set() 

    while (not solved): 
        i += 1
        next_paths = [] 
        for path in paths: 
            for button in buttons: 
                next_path = path.copy()
                for num in button: 
                    next_path[num] += 1
                if (check_joltage(next_path, min_joltage)): 
                    print("B")
                    solved = True 
                    break 
                if (''.join([str(v) for v in next_path]) not in visited): 
                    next_paths.append(next_path) 
                    visited.add(''.join([str(v) for v in next_path]))
            if (solved): 
                break 
        paths = next_paths
        print("i")

    button_presses += i

print(f"Puzzle 2: {button_presses}")

# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")