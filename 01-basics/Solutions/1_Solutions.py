# Solution and comments to the first exercise sheet (Introduction - Simple)

############### Exercise 1. Simple arithmetic ###############

3/5 + 2; 3/5 + 2.  # is integer division
3/float(5) + 2; 3/5. + 2  # is floating point division

3./5/2; 3/5./2   # floating point division, while:
3/5/2.   # first division is integer only second is floating point
5%2   # 5 modulo 2

############### Exercise 2. Find Errors ###############
# #!/usr/bin/env python
#
# import sys, random
# def compute(n):
#     i = 0; s = 0
#     while i < n:
#         s += random.random()
#         i += 1
#     return s/n
#
# n = int(sys.argv[1])
# print 'the average of %d random numbers is %g' % (n, compute(n))

############### Exercise 3.1. Logical expressions ###############

a = b = 1  # a)
a = 0; b = 1  # b)
a = 0; b = 0  # c)
a = 1; b = 0  # c)
a = 0; b = 1  # c)
a = 1; b = 1  # d)
a = 1; b = 0  # d)
a = 0; b = 1  # d)
a = 1; b = 1  # e)
a = 1; b = 0  # e)
a = 0; b = 0  # e)
a = b = 0  # f)
a = b = 1  # g) is equivalent to a)
a = 1; b = 1  # h) no it doesn't depend on b
a = 1; b = 0  # h)
a = b = c = 1  # i)
a = b = 1; c = 0  # j)
a = b = 1; c = 1  # j)
a = b = 0; c = 1  # j)
a = 0; b = 1; c = 1  # j)
a = 1; b = 0; c = 1  # j)
a = 1; b = c = 1  # k)
a = 1; b = 0; c = 1  # k)
a = 1; b = 1; c = 0  # k)
a = b = 1; c = 0  # l) is equivalent to j)
a = b = 1; c = 1  # l)
a = b = 0; c = 1  # l)
a = 0; b = 1; c = 1  # l)
a = 1; b = 0; c = 1  # l)


############### Exercise 3.2 ###############
fname = raw_input ("Please, type in your first name: ")
lname = raw_input ("Please, type in your last name: ")
phone = raw_input ("Please, type in your phone number: ")

if fname and lname and phone:
     print "Thank you!"
else:
     print "Do not leave any fields empty"


############### Exercise 3.3 ###############
# guess a number

answer = input("Please enter a number: ")

if answer == 5:
        print "My lucky number."
elif answer > 10:
        print "What a large number!"
else:
        print "That's not my lucky number."


############### Exercise 3.4 ###############
# not that although the values are the same 'is' detects a difference in type.
# so 'is' will give true only if value and object type are the same


############### Exercise 4.1 ###############

print "4. Program flow - Exercise 1" 
x = 0
for i in range(100):
    x += 1

print "1 summed a 100 times: %d\n" % x



############### Exercise 4.2 ###############

print "4. Program flow - Exercise 2"
x = 0
for i in range(1,101):
    x += i

print "Numbers summed up from 1 to 100: %d\n" % x


############### Exercise 4.3 ###############

print "4. Program flow - Exercise 3"
word1 = 'gateman'
word2 = ''
for i in range(len(word1)-1,-1,-1):
    word2 += word1[i]

print "Original word was: " + word1 + " and inverted version is: " + word2+"\n"

# Alternative, very elegant solution without for loop:

print "Inversion of the word with one command only: " +word1[::-1]+"\n"


############### Exercise 5.1 ###############
# a) with list comprehensions:
lst = [['a','b','c'],['d','e'],['f']]

flat=[item for sublist in lst for item in sublist]
print "Flattened with list comprehension:"
print flat

# b) with command 'reduce'
flat=reduce(lst.__add__,lst)
print "Flattened with reduce:"
print flat

# c) with a for loop
flat=[]
for sublist in lst:
  flat += sublist 
print "Flattened with for loop:"
print flat


############### Exercise 5.2 ###############
celebs = ["Albert Einstein", "Karl Marx", "Mohandas Karamchand Gandhi",
          "Alan Mathison Turing","Miles Dewey Davis III."]

print "The following people are famous:", celebs

new_celeb = raw_input("Type the name of another celebrity: ")
celebs.append(new_celeb)
print "The following people are famous:", celebs

number = input("Enter a number: ")
print "The celebrity number", number, "is", celebs[number-1]

celebs = ["Mario", "Luigi"] + celebs
print "The following people are famous:", celebs

del celebs[-1]
print "The following people are famous:", celebs

another_celeb = raw_input("Enter the name of a celebrity to be added/deleted: ")
if another_celeb in celebs:
        celebs.remove(another_celeb)
else:
        celebs.append(another_celeb)

print "The following people are famous:", celebs

more_celebs = celebs[:]

more_celebs.reverse()
print celebs
print more_celebs


############### Exercise 5.3 ###############
celebs = ["Albert Einstein", "Karl Marx", "Mohandas Karamchand Gandhi",
          "Alan Mathison Turing","Miles Dewey Davis III."]

for celeb in celebs:
    print "Hello", celeb + ", how are you?"


