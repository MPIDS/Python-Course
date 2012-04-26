li1=[(1,2),(4,1),(5,3)]
li2=li1[:]

def last(x):
    return x[-1]

def summed(x):
    return x[0] + x[1]


li1.sort(key=lambda x: x[-1])
li2.sort(key=last)
print li1
print li2

li1.sort(key=lambda x: x[-1]+x[0])
li2.sort(key=summed)
print li1
print li2
