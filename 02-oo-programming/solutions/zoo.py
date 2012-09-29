import animal

class Zoo:
    """This zoo collects animals which have a name."""
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
        for i in xrange( len(self.inhabitants),len(self.inhabitants)+nAnimals ):
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
        - lambda x: isinstance(x,animal.Cat)
        """

        inh = self.inhabitants # abbreviation
        return [ inh[x] for x in inh if filter(inh[x]) ]

    def visitorSelect(self):
        inp = raw_input()
        return self.select( lambda x: eval(inp) )

    def __getitem__(self,name):
        return self.inhabitants[ name ]
    
def test_zoo():
    z1=Zoo()
    z1.add( ("snowball",animal.Cat(3.14,3)) )

    z2=Zoo()
    z2.add( ("salmon",animal.Fish(1.2,1)) )
    z2.add( ("jellyfish",animal.Fish(2.7,2)) )

    print "Second zoo has %u inhabitants." % len(z2)
    print "Is first zoo smaller than second zoo?", z1<z2

    z1["snowball"].speak()

    z1.addMany(animal.Cat, 100)
    z1.addMany(animal.Fish,100)
    z1.rename("1","icecube")

    youngAnimals = z1.select(lambda x: x.age()<2)
    weirdAnimals = z1.select(lambda x: x.age()+x.weight()<=3.14)
    allCats = z1.select(lambda x: isinstance(x,animal.Cat) )
    print len(youngAnimals), len(weirdAnimals), len(allCats)

    visitorsAnimals = z1.visitorSelect()
    print "You visit %u animals." % len(visitorAnimals)

if __name__=='__main__':
    test_zoo()
