# README ------------------------------------------------------------------------------------------
# 
#   file: 04-printing-department.py
#   desc: day 4 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/4
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time 

parser = argparse.ArgumentParser() 
parser.add_argument("-d", "--data", help="path to .txt file dataset for challenge")
args = parser.parse_args() 

with open(args.data, "r") as file: 
    paper = file.readlines()
    paper = [row.replace('\n', '') for row in paper]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)


# part 1 ------------------------------------------------------------------------------------------

paper_counter = 0 

n_rows = len(paper) 
n_cols = len(paper[0])

## for each paper... 
for i in range(n_rows): 
    for j in range(n_cols): 

        ## if no paper in position, skip 
        if (paper[i][j] != "@"): 
            continue
        
        occupied = 0 
        ## for each possible position (8 maximum) around paper, count occupied spaces
        start_row = max(0, i-1)
        start_col = max(0, j-1)

        row = start_row
        col = start_col

        while (row < n_rows) and (row <= i+1): 
            while (col < n_cols) and (col <= j+1): 
                if ((row != i) or (col != j)) and (paper[row][col] == "@"):
                    occupied += 1
                col += 1
            row += 1
            col = start_col

        if (occupied < 4): 
            paper_counter += 1

print(f"Puzzle #1: {paper_counter}")


# part 2 ------------------------------------------------------------------------------------------

removed_counter = 0 

n_rows = len(paper) 
n_cols = len(paper[0])

removed = True 
while (removed): 

    removed = False 

    for i in range(n_rows): 
        for j in range(n_cols): 

            ## if no paper in position, skip 
            if (paper[i][j] != "@"): 
                continue
            
            occupied = 0 
            ## for each possible position (8 maximum) around paper, count occupied spaces
            start_row = max(0, i-1)
            start_col = max(0, j-1)

            row = start_row
            col = start_col

            while (row < n_rows) and (row <= i+1): 
                while (col < n_cols) and (col <= j+1): 
                    if ((row != i) or (col != j)) and (paper[row][col] == "@"):
                        occupied += 1
                    col += 1
                row += 1
                col = start_col

            if (occupied < 4): 
                removed_counter += 1
                removed = True 
                paper[i] = paper[i][:j] + "." + paper[i][(j+1):]

print(f"Puzzle #2: {removed_counter}")


# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")