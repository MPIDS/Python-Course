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

    def addMany(self, Species, nAnimals):
        from random import random,randint
        for i in xrange(nAnimals):
            self.inhabitants[str(i)] = Species(10*random() # weight
                                               , randint(0,50) # age
                                               )
    def rename(self, oldName, newName):
        self.inhabitants[newName] = self.inhabitants[oldName]
        del self.inhabitants[oldName]

    def select(self, filter):
        """
        Examples for filter:
        - lambda x: x.age()<2
        - lambda x: x.age()+x.weight()<3.142
        - lambda x: type(x)==Cat
        """

        inh = self.inhabitants # abbreviation
        return [ inh[x] for x in inh if filter(inh[x]) ]

    def visitorSelect(self):
        inp = raw_input()
        return self.select( lambda x: eval(inp) )

    def __getitem__(self,name):
        return self.inhabitants[ name ]
    
