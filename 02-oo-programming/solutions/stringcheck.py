class stringcheck:
    """Checks if a given string is contained in the member string"""
    def __init__(self, mystring):
        self.mystring=mystring

    def check(self, other):
        if other in self.mystring:
            return True
        else:
            return False
