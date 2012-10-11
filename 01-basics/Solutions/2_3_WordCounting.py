#!/usr/bin/python

from string import split
from operator import itemgetter

# Word Counting - Part 1
f = open("RobinHood.txt")

lines = f.readlines()

num_lines = len(lines)

num_words = num_chars = 0
for s in lines:
    num_words += len(split(s,' '))
    num_chars += len(s)

# Word Counting - Part 2
f_save = open("RobinHood_Statistics.txt",'w')

f_save.write("Number of lines: %d, number of words: %d, number of characters: %d" % (num_lines, num_words, num_chars))
f_save.close()

# Word Counting - Part 3
f.seek(0)
words = split(f.read(),' ')
words_dict = {}
for i in range(len(words)):
    if words[i] in words_dict:
        words_dict[words[i]] += 1
    else:
        words_dict[words[i]] = 1
    
tmp = words_dict.items()
tmp.sort(key=itemgetter(1))

print tmp[-10:]
f.close()
