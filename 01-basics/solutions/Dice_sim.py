
#!/usr/bin/python3

from random import randint
from sys import argv
from math import factorial
import csv

# Run external script - Part 1

# Check if 2 arguments are passed, otherwise stop execution
# note that first argument is always the script name thus in total there are 3 arguments
assert(len(argv) == 3)

N = int(argv[1])
n = int(argv[2])

counter = 0
for i in range(n):
    for j in range(N):
        dice = randint(1,6)
        if dice == 6:
            counter += 1
            break  # it is enough that one dice out of N gives a 6, that is how we have defined the event
        
# calculate the probability theoretical probability
# using a list comprehension to produce a binomial distribution
prob = sum([float(factorial(N))/(factorial(k)*factorial(N-k))*(1./6)**k * (5./6)**(N-k) for k in range(1,N+1)])

experiment = (N, n, float(counter)/n,prob)
# print(results such that the external script can read them via stdout)
print(experiment)

# Run external script - Part 2
csvfile = open("DiceExperiment_Results.csv","a")
csv_output = csv.writer(csvfile)
csv_output.writerow(experiment)
csvfile.close()