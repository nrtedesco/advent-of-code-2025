# README ------------------------------------------------------------------------------------------
# 
#   file: 05-cafeteria.py
#   desc: day 5 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/5
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time 

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    ingredients = file.readlines()
    ingredients = [row.replace('\n', '') for row in ingredients]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)

## split data into fresh ingredient listings vs. requested ingredient IDs 
split_idx = 0 
while (ingredients[split_idx] != ""):
    split_idx += 1

fresh_ranges = ingredients[:split_idx] 
requested = ingredients[(split_idx+1):]

## parse fresh ranges into lows and highs 
parsed_fresh_ranges = []

for r in fresh_ranges: 
    low, high = r.split("-") 
    parsed_fresh_ranges.append([int(low), int(high)])


# part 1 ------------------------------------------------------------------------------------------

## determine # of requested ingredients which are fresh 
fresh_req_counter = 0 
for req in requested: 
    req = int(req) 
    for low, high in parsed_fresh_ranges: 
        if (req >= low) and (req <= high): 
            fresh_req_counter += 1
            break 

print(f"Puzzle 1: {fresh_req_counter}")


# part 2 ------------------------------------------------------------------------------------------

## strategy: iterate over "input ranges", representing potentially overlapping ranges. 
##           - iteration L1: full pass through candidate input ranges to check for overlap 
##           - iteration L2: check if individual input range overlaps output ranges
##                           - if so, combine with appropriate range and append to growing output ranges
##                           - if not, simply append to growing output ranges 
##           - iteration L3: within each input range, iterate over current output ranges to check for overlap

input_ranges = parsed_fresh_ranges
overlap = True 

while (overlap): 
    
    overlap = False 
    combined_ranges = [] 

    for low, high in input_ranges: 

        combine = False 
        rm_indices = [] 

        for i, (l, h) in enumerate(combined_ranges): 
            
            # case 1: incoming low falls within bounds for existing range 
            if (low >= l) and (low <= h): 
                combine = True 
                overlap = True
                if (high > h): 
                    combined_ranges[i][1] = high 
                break 
            
            # case 2: incoming high falls within bounds for existing range 
            if (high >= l) and (high <= h): 
                combine = True 
                overlap = True
                if (low < l): 
                    combined_ranges[i][0] = low 
                break 

            # case 3: incoming range completely overshadows existing range 
            if (low <= l) and (high >= h): 
                overlap = True
                rm_indices.append(i) 

        # remove overshadowed ranges 
        combined_ranges = [r for i, r in enumerate(combined_ranges) if (i not in rm_indices)]

        # if incoming range was not part of combination, add as new item
        if (not combine): 
            combined_ranges.append([low, high])

    # update list of potentially overlapping ranges for next pass
    input_ranges = combined_ranges
        
## given distinct fresh ranges, calculate total ingredients
total_fresh = 0 
for low, high in combined_ranges: 
    total_fresh += (high - low + 1) 

print(f"Puzzle 2: {total_fresh}")


# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")