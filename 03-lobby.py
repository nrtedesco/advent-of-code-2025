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

## if joltages are always 12 digits long, we can take advantage of digit position to determine max
## for example, if bank is 18 digits long, we know first digit is max of possible first digits (0-6)

results = [] 
start_index = 0

for bank in banks: 

    start_index = 0
    joltage = "" 

    for p in range(12): 

        candidate_digits = bank[start_index:len(bank)-(11-p)]

        max_digit = -1 
        max_index = -1 

        for index, digit in enumerate(candidate_digits): 
            digit = int(digit)
            if (digit > max_digit): 
                max_digit = digit 
                max_index = start_index + index 

        joltage += str(max_digit) 
        start_index = max_index + 1

    results.append(int(joltage))

final_joltage = sum(results)

print(f"Puzzle #2: {final_joltage}")


# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")