class String:
    """Checks if a given string is contained in the member string"""
    counter = 0
    def __init__(self, mystring):
        self.mystring=mystring
        String.counter += 1

    def __del__(self):
        String.counter -= 1

    def check(self, other):
        if other in self.mystring:
            return True
        else:
            return False

s1=String("Hello")
s2=String("World")

print s1.check("el"), s2.check("el")

print "There are %u String instances" % String.counter

del s2
print "Now: %u String instances" % String.counter

s1=1
print "And now: %u" % String.counter
