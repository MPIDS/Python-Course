import animal

class Zoo:
    """This zoo collects same animals which have a name."""
    def __init__(self):
        self.inhabitants = {}

    def __len__(self):
        return len( self.inhabitants )

    def __cmp__(self, rhs):
        if not isinstance(rhs, Zoo):
            print "I can only compare Zoos."
            return
        
        mylen = len(self)
        rhslen = len(rhs)
        if mylen<rhslen : return -1
        elif mylen==rhslen: return 0
        else: return 1

    def add(self,rhs):
        #check if rhs has correct format
        if not isinstance(rhs, tuple):
            print "Argument is no tuple."
            return
        if not isinstance(rhs[0], str):
            print "First part of tuple must be a string."
            return
        if not isinstance(rhs[1], animal.Animal):
            print "Second part of tuple must be an animal."
            return
        
        self.inhabitants[ rhs[0] ] = rhs[1]

    def __getitem__(self,name):
        return self.inhabitants[ name ]
    
