#!/usr/bin/python

from random import randint

# Dice Simulation 1
n = int(raw_input("How many iterations should I perform?\n"))

counter = 0
for i in range(n):
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    if dice1 == 6 or dice2 == 6:
        counter += 1

print "Estimated probability of getting a 6 if two dice are thrown: %f and exact result is: %f" % (float(counter)/n,11./36)
# n = 100000 leads to a correct result up to 3 decimals.


# Dice Simulation 2

N = int(raw_input("How many dice should I roll?\n"))
n = int(raw_input("How many iterations should I perform?\n"))

counter = 0
for i in range(n):
    for j in range(N):
        dice = randint(1,6)
        if dice == 6:
            counter += 1
            break  # it is enough that one dice out of N gives a 6, that is how we have defined the event
        
# calculate the probability theoretical probability
from math import factorial
# using a list comprehension to produce a binomial distribution
prob = sum([float(factorial(N))/(factorial(k)*factorial(N-k))*(1./6)**k * (5./6)**(N-k) for k in range(1,N+1)])
print "Estimated probability of getting a 6 if %d dice are thrown: %f and exact result is: %f" % (N,float(counter)/n, prob)


# Dice Simulation 3

n = int(raw_input("How many repititions of the game do we play?\n"))

money = 0
for i in range(n):
    if sum([randint(1,6) for i in range(4)]) < 9:
        money += 10
    else:
        money -= 1
        
if money < 0:
    print "You lost %d amount of money" % (-money)
else:
    print "You won %d amount of money" % (money)

# You will lose on the long run, better not to play the game.

