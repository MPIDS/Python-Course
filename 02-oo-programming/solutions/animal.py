class Animal:
    """An abstract animal"""

    def __init__(self, weight, age):
        # store your own copy of weight and age such that we can 
        # refer to them later
        self.__weight=weight
        self.__age = age

        # look at move() function
        self._weightLossPerDistance = 1.0

    def age(self):
        """ This function allows to access self.__age from outside """
        return self.__age

    def weight(self):
        """ This function allows to access self.__weight from outside """
        return self.__weight

    def eat(self, amount):
        """ When the animal eats, it inceases the weight by amount. """
        self.__weight += amount

    def move(self, distance):
        """ Motion needs energy, therefore this function decreases the 
        weight according to the constant self.__weightLossPerDistance.
        If self.__weight falls below 0 an error message is printed. 
        """
        self.__weight -= self._weightLossPerDistance*distance
        if self.__weight<=0.0:
            print "I'm starving..."

    def speak(self):
        print "I am an abstract animal which can't speak"

class Fish(Animal):
    """This is a fish"""

    def __init__(self, weight, age):
        # Call the constructor of the parent class
        Animal.__init__(self, weight, age)

    def move(self, distance):
        # Use the behaviour from the parent class, and, in addition,
        # print a fish-specific message
        Animal.move(self, distance)
        print "I'm swimming through the aquarium"

    def speak(self):
        print "blub"

class Cat(Animal):
    """I'm a cat"""

    def __init__(self, weight, age):
        Animal.__init__(self, weight, age)
        self._weightLossPerDistance = 3.0

    def move(self, distance):
        Animal.move(self, distance)
        print "I'm chasing mice"

    def speak(self):
        print "Miau"

    def eat(self, fish, animalDi):
        """
        This function checks if the argument 'fish' really is of type Fish
        and, if so, eats it. This accounts to deleting it from the dictionary
        'animalDi'. Note that it is (as far as I know) not possible to 
        globally erase the fish instance from memory. So deleting it from
        a "reservoir of animals" is the closest thing to killing it.
        """
        if isinstance(fish,Fish):
            delvar=None
            for a in animalDi:
                if id(fish)==id(animalDi[a]):
                    delvar=a
                    break
            if delvar!=None:
                del animalDi[a]
                print "Hmmm, that was delicious. Rest in peace fish!"
            else:
                print "Couldn't see the fish to eat"
        else:
            print "I'm a cat, I don't eat that crap"

def test_animal():
    a=Animal(27.23,1)
    f=Fish(3.141,2)
    c=Cat(2.718,3)

    pets = {
        'abstract':a,
        'neo':f,
        'snowball':c
        }

    for p in pets:
        pets[p].speak()
        pets[p].move(2)
    
    c.eat(a,pets)
    c.eat(f,pets)
    try:
        pets['neo'].speak()
    except(KeyError):
        print "Sorry, the fish is gone"

    # but accessing f directly still works:
    f.speak()
        
if __name__=='__main__':
    test_animal()
