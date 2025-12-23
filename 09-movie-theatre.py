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
    red_tiles = [r for r in csv.reader(file)]

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)

red_tiles = np.array(red_tiles).astype(int)


# part 1 ------------------------------------------------------------------------------------------

## compute area for each tile pair, keeping track of max

max_area = -1
for i in range(len(red_tiles)): 
    for j in range(i+1, len(red_tiles)): 
        curr_area = np.prod(np.abs(red_tiles[i] - red_tiles[j]) + 1)       # must add 1 since rectangle is inclusive of bounds
        if (curr_area > max_area): 
            max_area = curr_area 

print(f"Puzzle #1: {max_area}")


# part 2 ------------------------------------------------------------------------------------------

## compress coordinates 
x_sorted = np.sort(np.unique([t[0] for t in red_tiles]))
y_sorted = np.sort(np.unique([t[1] for t in red_tiles]))

coords = [] 
for t in red_tiles: 
    x_new = np.argwhere(x_sorted == t[0])[0][0].item() 
    y_new = np.argwhere(y_sorted == t[1])[0][0].item() 
    coords.append([x_new, y_new])

coords = np.array(coords) 

## plot red tiles in compressed space 
floor_shape = np.max(coords, axis=0)[::-1] + 1
floor = np.full(floor_shape, '.', dtype=object)

for x, y in coords: 
    floor[y, x] = '#'

## add green border tiles 
for x, y in coords: 

    # find next tile to the right 
    i = 1 
    while (y + i < floor.shape[0]): 
        if (floor[y + i, x] == '#'): 
            for v in range(y + 1, y + i): 
                floor[v, x] = 'X'
            break 
        i += 1

    # find next tile below 
    i = 1 
    while (x + i < floor.shape[1]): 
        if (floor[y, x + i] == '#'): 
            for v in range(x + 1, x + i): 
                floor[y, v] = 'X'
            break 
        i += 1

## flood fill outside with negative spaces 
Y, X = floor.shape 
stack = []
for x in range(X): 
    for y in range(Y): 
        if (x == 0) or (x == X - 1) or (y == 0) or (y == Y - 1): 
            if (floor[y, x] not in ['X', '#']): 
                floor[y, x] = '!'
                stack.append((x, y))

while (len(stack) > 0): 
    x, y = stack.pop() 
    ## check up / down / left / right
    if (y + 1 < Y) and (floor[y + 1, x] not in ['X', '#', '!']): 
        floor[y + 1, x] = '!' 
        stack.append((x, y + 1)) 
    if (y - 1 > 0) and (floor[y - 1, x] not in ['X', '#', '!']): 
        floor[y - 1, x] = '!' 
        stack.append((x, y - 1))
    if (x + 1 < X) and (floor[y, x + 1] not in ['X', '#', '!']): 
        floor[y, x + 1] = '!' 
        stack.append((x + 1, y)) 
    if (x - 1 > 0) and (floor[y, x - 1] not in ['X', '#', '!']): 
        floor[y, x - 1] = '!' 
        stack.append((x - 1, y))

## iterate over tile pairs. check if rectangle is valid, then check area against max 

max_area = -1
for i in range(len(red_tiles)): 
    t1 = red_tiles[i]
    for j in range(i+1, len(red_tiles)): 
        t2 = red_tiles[j]

        valid = True 

        start_x = np.argwhere(x_sorted == min(t1[0], t2[0]))[0][0].item() 
        start_y = np.argwhere(y_sorted == min(t1[1], t2[1]))[0][0].item()
        end_x = np.argwhere(x_sorted == max(t1[0], t2[0]))[0][0].item()
        end_y = np.argwhere(y_sorted == max(t1[1], t2[1]))[0][0].item()  

        for x in range(start_x, end_x + 1): 
            for y in range(start_y, end_y + 1): 
                if (floor[y][x] == '!'): 
                    valid = False 
                    break 

        if (valid): 
            curr_area = np.prod(np.abs(t1 - t2) + 1)       # must add 1 since rectangle is inclusive of bounds
            if (curr_area > max_area): 
                max_area = curr_area 

print(f"Puzzle #2: {max_area}")



# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")