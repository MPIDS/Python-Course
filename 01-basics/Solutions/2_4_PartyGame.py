#!/usr/bin/python
from random import randint

secret_num = randint(0,99)
print secret_num
interval = [0,99]
while 1:
    guessed_num = int(raw_input("State a number between %d and %d: " % tuple(interval)))
    if guessed_num > interval[1]:
        print "Number is to large, we said between %d and %d" % tuple(interval)
    elif guessed_num < interval[0]:
        print "Number is to small, we said between %d and %d" % tuple(interval)
    elif guessed_num == secret_num:
        print "Soooory, you hit the number - haha, you have to kiss your neighbor! Okay, let's say only on the cheek."
        break
    elif guessed_num < secret_num:
        interval[0] = guessed_num
    elif guessed_num > secret_num:
        interval[1] = guessed_num
        
    if interval[0]+1 == secret_num and interval[1]-1 == secret_num:
        print "Okay, you won. I'll do the silly dance for you if you provide me with legs."
        break
