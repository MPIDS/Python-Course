class Animal:
    """An abstract animal"""

    def __init__(self, weight, age):
        self.__weight=weight
        self.__age = age
        self._weightLossPerDistance = 0.0

    def age(self):
        return self.__age

    def weight(self):
        return self.__weight

    def eat(self, amount):
        self.__weight += amount

    def move(self, distance):
        self.__weight -= self._weightLossPerDistance*distance
        if self.__weight<=0.0:
            print "I'm starving..."

    def speak(self):
        print "I am an abstract animal which can't speak"

class Fish(Animal):
    """This is a fish"""

    def __init__(self, weight, age):
        Animal.__init__(self, weight, age)
        self._weightLossPerDistance = 1.0

    def move(self, distance):
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

class Zoo:
    """I'm full of animals"""
    
    def __init__(self):
        pass

    def __add__(self, dict):
        pass
