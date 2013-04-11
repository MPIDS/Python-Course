f=open("test.csv","r")
values=[float(x) for x in f.read().split(",")]
print values
