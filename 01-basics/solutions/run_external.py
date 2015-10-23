#!/usr/bin/python3

import subprocess as sp
import os

# note: script you call must be executable otherwise an error will be raised
# use strip() to remove the newline character \n
script_result =  sp.check_output(["python", "Dice_sim.py", '5', '1000'], env={'PATH': os.environ['PATH']})

# Run external script - Part 3
from sys import argv
import os
# remove csv-file if already existing to save only new experiments
if os.path.isfile('DiceExperiment_Results.csv'):
    os.remove('DiceExperiment_Results.csv')
    
# Check if 2 arguments are passed, otherwise stop execution
# note that first argument is always the script name thus in total there are 3 arguments
assert(len(argv) == 3)

arg1, arg2 = argv[1:]
print(arg1 + " aha" + arg2)
# get rid of initial N= and n= and extract numbers separated by colon
# store the number list temporarily in variables
tmp1 = arg1[2:].split(':')
tmp2 = arg2[2:].split(':')

print(["und nun:"] + tmp1 + tmp2)
if len(tmp1) == 2:
    N_list = range(int(tmp1[0]),int(tmp1[1])+1)
else:
    # add another step size to stopping value such that MATLAB behaviour is achived
    N_list = range(int(tmp1[0]),int(tmp1[2])+int(tmp1[1]),int(tmp1[1]))

if len(tmp2) == 2:
    n_list = range(int(tmp2[0]),int(tmp2[1])+1)
else:
    # add another step size to stopping value such that MATLAB behaviour is achived
    n_list = range(int(tmp2[0]),int(tmp2[2])+int(tmp2[1]),int(tmp2[1]))

for N in N_list:
    for n in n_list:
        sp.call(['python', './Dice_sim.py', str(N), str(n)], env={'PATH': os.environ['PATH']})