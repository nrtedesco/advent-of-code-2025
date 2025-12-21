# README ------------------------------------------------------------------------------------------
# 
#   file: 08-playground.py
#   desc: day 8 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/8
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
    junction_data = [l for l in csv.reader(file)]

n_connections = int(args.n_connections)

start_time = time.time() 
print("\nStarting Script\n" + "---" * 40)

## calculate pairwise distance between all points
distances = []  
for i in range(len(junction_data)): 
    i_distances = [] 
    val1 = np.array(junction_data[i]).astype(int)
    for j in range(len(junction_data)): 
        val2 = np.array(junction_data[j]).astype(int)
        temp_distance = np.sqrt(np.sum((np.array(val1) - np.array(val2)) ** 2))
        i_distances.append(temp_distance) 
    distances.append(i_distances) 

distances = np.array(distances) 

## black out diagonal elements 
for i in range(len(distances)): 
    distances[i, i] = np.inf 

reference_distances = distances.copy() 


# part 1 ------------------------------------------------------------------------------------------

## iteratively construct junction box circuits based on minimized distance 
circuits = [] 
for n in range(n_connections): 

    ## determine current shortest pair + translate to valid indices 
    shortest_pair = np.argmin(distances) 
    i = shortest_pair // len(distances) 
    j = shortest_pair % len(distances)

    ## iterate over existing circuits, and define new circuits with following logic.
    ## given junction box pair (junction1, junction2)...
    ## - if junction1 in existing circuit: 
    ##   - if junction2 in another existing circuit, create new combined circuit
    ##   - else, add junction2 to junction1 existing circuit 
    ## - repeat process for junction2
    ## - if neither junction1 nor junction2 in existing circuit, create new circuit 

    seen1 = False
    for k, circuit1 in enumerate(circuits): 

        if (i in circuit1) and (j not in circuit1): 

            seen2 = False
            for l, circuit2 in enumerate(circuits): 
                if (k == l): 
                    continue 
                if (j in circuit2): 
                    seen2 = True
                    for val in circuit2: 
                        circuit1.add(val) 
                    circuits = circuits[:l] + circuits[l+1:]
                    break

            if (not seen2): 
                circuit1.add(j)

            seen1 = True
            break

        elif (j in circuit1) and (i not in circuit1): 

            seen2 = False
            for l, circuit2 in enumerate(circuits): 
                if (k == l): 
                    continue 
                if (i in circuit2): 
                    seen2 = True
                    for val in circuit2: 
                        circuit1.add(val) 
                    circuits = circuits[:l] + circuits[l+1:]
                    break

            if (not seen2): 
                circuit1.add(i) 

            seen1 = True
            break

        elif (i in circuit1) and (j in circuit1): 
            seen1 = True 
            break
    
    ## if neither member of shortest pair was present in any existing circuit, create new circuit
    if (not seen1): 
        circuits.append(set([i, j]))

    ## blacklist current shortest distance prior to next iteration
    distances[i, j] = np.inf
    distances[j, i] = np.inf

## multiply sizes of three largest circuits for solution 
circuit_sizes = [len(circuit) for circuit in circuits]
circuit_sizes.sort(reverse=True) 

solution1 = 1 
for val in circuit_sizes[:3]:
    solution1 *= val

print(f"Puzzle 1: {solution1}")

# part 2 ------------------------------------------------------------------------------------------

## reset distances to original reference 
distances = reference_distances.copy()

## iteratively construct junction box circuits based on minimized distance... 
## continue until we only have a single circuit connecting all junction boxes
circuits = [] 
n_junction_boxes = len(distances)
while (len(circuits) == 0) or (len(circuits[0]) < n_junction_boxes): 

    ## determine current shortest pair + translate to valid indices 
    shortest_pair = np.argmin(distances) 
    i = shortest_pair // len(distances) 
    j = shortest_pair % len(distances)

    ## iterate over existing circuits, and define new circuits with following logic.
    ## given junction box pair (junction1, junction2)...
    ## - if junction1 in existing circuit: 
    ##   - if junction2 in another existing circuit, create new combined circuit
    ##   - else, add junction2 to junction1 existing circuit 
    ## - repeat process for junction2
    ## - if neither junction1 nor junction2 in existing circuit, create new circuit 

    seen1 = False
    for k, circuit1 in enumerate(circuits): 

        if (i in circuit1) and (j not in circuit1): 

            seen2 = False
            for l, circuit2 in enumerate(circuits): 
                if (k == l): 
                    continue 
                if (j in circuit2): 
                    seen2 = True
                    for val in circuit2: 
                        circuit1.add(val) 
                    circuits = circuits[:l] + circuits[l+1:]
                    break

            if (not seen2): 
                circuit1.add(j)

            seen1 = True
            break

        elif (j in circuit1) and (i not in circuit1): 

            seen2 = False
            for l, circuit2 in enumerate(circuits): 
                if (k == l): 
                    continue 
                if (i in circuit2): 
                    seen2 = True
                    for val in circuit2: 
                        circuit1.add(val) 
                    circuits = circuits[:l] + circuits[l+1:]
                    break

            if (not seen2): 
                circuit1.add(i) 

            seen1 = True
            break

        elif (i in circuit1) and (j in circuit1): 
            seen1 = True 
            break
    
    ## if neither member of shortest pair was present in any existing circuit, create new circuit
    if (not seen1): 
        circuits.append(set([i, j]))

    ## blacklist current shortest distance prior to next iteration
    distances[i, j] = np.inf
    distances[j, i] = np.inf

## multiply x-coordinates of final two connected junction boxes
solution2 = int(junction_data[i][0]) * int(junction_data[j][0])

print(f"Puzzle 2: {solution2}")
    

# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")