# README ------------------------------------------------------------------------------------------
# 
#   file: 06-trash-compactor.py
#   desc: day 6 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/6
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time 

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    math_hw = file.readlines()
    math_hw = [row.replace('\n', '') for row in math_hw]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)


# part 1 ------------------------------------------------------------------------------------------

## parse into separate problems (does not preserve spacing) 
problems = [] 
for i, row in enumerate(math_hw): 
    for j, col in enumerate(row.split()): 
        if (i == 0): 
            problems.append([col]) 
        else: 
            problems[j].append(col)

## solve each math problem, then add to total
total = 0 
for components in problems: 

    if (components[-1] == "*"): 
        solution = 1 
        for val in components[:-1]: 
            solution *= int(val)
    elif (components[-1] == "+"): 
        solution = 0
        for val in components[:-1]: 
            solution += int(val)
    else: 
        raise Exception("operation not in expected set (+, *)")
    
    total += solution
    
print(f"Puzzle #1: {total}") 


# part 2 ------------------------------------------------------------------------------------------

## parse into separate problems by identifying split indices (preserves spacing) 
split_indices = [] 

n_components = len(math_hw) - 1           # exclude operations row 
n_problems = len(math_hw[0].split())      # number of distinct problems within document

lookup_table = []                         # convert math homework from list of strings to nested list
for line in math_hw: 
    lookup_table.append(line.split())

for p in range(n_problems):               # for each problem, search over components to determine max length number
    longest_num = 0 
    for c in range(n_components): 
        if (len(lookup_table[c][p]) > longest_num): 
            longest_num = len(lookup_table[c][p]) 
    split_indices.append(longest_num) 

problems_with_spaces = []                 # parse math homework into nested list of problems,
for i, line in enumerate(math_hw):        # where each problem is a list of components (with spacing preserved)
    for j, idx in enumerate(split_indices): 
        num_with_space = line[:idx]
        if (i == 0): 
            problems_with_spaces.append([num_with_space])
        elif (i < len(math_hw) - 1): 
            problems_with_spaces[j].append(num_with_space)
        else: 
            problems_with_spaces[j].append(num_with_space.strip())
        line = line[(idx+1):]

## solve each math problem, then add to total 
total = 0 
for components in problems_with_spaces: 

    nums_with_spaces = components[:-1]
    operation = components[-1]

    # iterate over column positions of components in problem (ex: "356", " 23" -> 2, 1, 0)
    # to extract number corresponding to each column
    d = len(nums_with_spaces[0]) - 1    
    parsed_nums = [] 
    while (d >= 0): 
        num = "" 
        for component in nums_with_spaces: 
            num += component[d] 
        d -= 1
        parsed_nums.append(int(num.strip()))
    
    # solve problem according to operation
    if (operation == "+"): 
        solution = 0 
        for num in parsed_nums: 
            solution += num 
    elif (operation == "*"):
        solution = 1 
        for num in parsed_nums: 
            solution *= num 
    else: 
        raise Exception("operation not in expected set (+, *)")

    total += solution 

print(f"Puzzle #2: {total}")
    

# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")