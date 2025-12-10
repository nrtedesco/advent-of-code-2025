# README ------------------------------------------------------------------------------------------
# 
#   file: 03-lobby.py
#   desc: day 3 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/3
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
    banks = file.readlines()
    banks = [r.replace('\n', '') for r in banks]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)


# part 1 ------------------------------------------------------------------------------------------

results = [] 
for bank in banks: 

    max_joltage = -1

    for i in range(len(bank)): 
        for j in range(i+1, len(bank)): 
            temp_joltage = int(f"{bank[i]}{bank[j]}")
            if (temp_joltage > max_joltage): 
                max_joltage = temp_joltage

    results.append(max_joltage) 

final_joltage = sum(results)

print(f"Puzzle #1: {final_joltage}")


# part 2 ------------------------------------------------------------------------------------------