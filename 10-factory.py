# README ------------------------------------------------------------------------------------------
# 
#   file: 09-movie-theatre.py
#   desc: day 9 (parts 1 and 2) of advent of code 2025 https://adventofcode.com/2025/day/9
# 
# -------------------------------------------------------------------------------------------------

# setup -------------------------------------------------------------------------------------------

import argparse
import time
import z3

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

button_presses = 0 
for machine in manual: 
    # parse machine components (indicator lights + buttons) from line 
    desired_config  = machine.replace('[', '').replace(']', '').split()[0]
    raw_buttons = machine.split(']')[1].split('{')[0].replace('(', '').replace(')', '').split()
    buttons = []
    for button in raw_buttons: 
        buttons.append([int(v) for v in button.split(',')])

    # check edge case - starting position is desired position 
    start_config = ['.'] * len(desired_config)
    if (start_config == desired_config): 
        continue 

    # start BFS
    i = 0 
    paths = [start_config]
    solved = False

    while (not solved): 
        i += 1
        next_paths = [] 
        for path in paths: 
            for button in buttons: 
                next_path = path[:]
                for num in button: 
                    if (next_path[num] == '#'): 
                        next_path[num] = '.'
                    else: 
                        next_path[num] = '#'
                if (''.join(next_path) == desired_config): 
                    solved = True 
                    break 
                next_paths.append(next_path) 
            if (solved): 
                break 
        paths = next_paths 
    
    button_presses += i 

print(f"Puzzle 1: {button_presses}")


# puzzle 2 ----------------------------------------------------------------------------------------

## NOTE: wasn't able to figure this one out on my own, so used reddit + Z3 documentation to help me through it
## - source: https://www.reddit.com/answers/6c6648fb-00d8-4665-8c3a-621dc31b89ee/?q=Advent+of+Code+2025+Day+10+solutions&source=PDP&tl=en

button_presses = 0
for machine in manual: 

    # parse out machine components (joltage + buttons) 
    min_joltage = [int(v) for v in machine.split('{')[1].replace('}', '').split(',')]
    buttons = [[int(v) for v in b.split(',')] for b in machine.split(']')[1].split('{')[0].replace('(', '').replace(')', '').split()]

    # convert components to Z3 variables + optimization problem 

    optimizer = z3.Optimize()
    vars = [z3.Int(f"x{i}") for i in range(len(buttons))]

    ## constraint 1: all button counters should be at least 0 
    for var in vars: 
        optimizer.add(var >= 0)

    ## constraint 2: each respective button 
    for i in range(len(min_joltage)): 
        optimizer.add(sum(1 * vars[j] if i in buttons[j] else 0 * vars[j] for j in range(len(vars))) == min_joltage[i])

    ## minimize total button presses 
    t = z3.Int('t')
    optimizer.add(t == sum(vars)) 
    optimizer.minimize(t)
    
    if optimizer.check() == z3.sat:
        model = optimizer.model()
        button_presses += model.eval(t).as_long()
    else:
        raise Exception("no solution found")

print(f"Puzzle 2: {button_presses}")

# wrapup ------------------------------------------------------------------------------------------

end_time = time.time() 

print("---" * 40) 
print(f"Script Execution Time: {end_time - start_time:.04f}s\n")