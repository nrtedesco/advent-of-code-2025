# README ------------------------------------------------------------------------------------------
# 
#   file: 02-gift-shop.py
#   desc: day 2 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/2
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import csv 
import time 

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    file_reader = csv.reader(file) 
    data = [] 
    for row in file_reader: 
        data += row 

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)


# part 1 ------------------------------------------------------------------------------------------

## convert ID ranges to singular (ex: "123-126" -> ["123", "124", "125", "126"])
ids = [] 
for id_range in data: 

    id_min, id_max = id_range.split("-") 

    ids.append(id_min) 

    id_min = int(id_min) 
    id_max = int(id_max) 

    while (id_min < id_max): 
        id_min += 1
        ids.append(str(id_min)) 

## parse IDs to identify invalid -> should have sequence of digits repeated twice 
invalid_ids = [] 
for id in ids: 

    id_len = len(id) 
    midpoint = id_len // 2
    if (midpoint != id_len / 2): 
        continue 

    half1 = id[:midpoint] 
    half2 = id[midpoint:]

    if (half1 == half2): 
        invalid_ids.append(int(id)) 

## sum invalid IDs to get solution
solution1 = sum(invalid_ids) 
print(f"Puzzle #1: {solution1}")


# part 2 ------------------------------------------------------------------------------------------

invalid_ids = [] 
for id in ids: 

    id_len = len(id) 
    midpoint = id_len / 2

    temp_midpoint = 1
    while (temp_midpoint <= midpoint): 
        n_repeats = id_len / temp_midpoint 
        if (n_repeats == id_len // temp_midpoint): 
            repeat_val = id[:temp_midpoint] 
            n_repeats = int(n_repeats)
            if (repeat_val * n_repeats == id): 
                invalid_ids.append(int(id)) 
                break 
        temp_midpoint += 1

## sum invalid IDs to get solution
solution2 = sum(invalid_ids) 
print(f"Puzzle #2: {solution2}")


# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")