##### 0. Motivation for Object oriented approach

### 0.1 Combining data and functions

student1_name = 'Bob'
student2_name = 'Sarah'

student1_age = 25
student2_age = 26

# print record of all students
def printStudent(name, age):
    print '%s is %u years old' % (name, age)

printStudent(student1_name, student1_age)
printStudent(student2_name, student2_age)

# adding more students becomes more and more cumbersome
# One way out: using arrays
name = ['Bob', 'Sarah', 'Joe']
age  = [25, 26, 27]

def printAllStudents():
    for i in range( len(name) ):
        printStudent(name[i], age[i])

printAllStudents()

# Still a bit annoying: adding more attributes to a student requires a
# change of printStudent AND printAllStudent:

program = ['Physics', 'Politics', 'Sociology']

def printStudent2(name, age, program):
    print '%s is %u years old' % (name, age, program)

def printAllStudents2():
    for i in range( len(name) ):
        printStudent(name[i], age[i], program[i])

# What we need is a way to combine data and functions -> Classes
# Another example: Univesity administration: provides functionality
# like: enroll(), registerForExam()
# this functionality is imtimately related to some underlying data:
# a database of students

### 0.2 Privacy

grade=[1, 2, 6]
def IDontLikeMyGrade(studentID):
    grade[studentID] = 1

# Is there a way to prevent this?

### 0.3 Inheritance

# Example: We want to create a zoo-simulator
# So we would like some code ('objects') to represent animals. All animals have
# some things in common (all have a name, all have a weight, and an age,
# all can move. But: moving means different things for different animals.
# A fish swims, a sparrow flies, a penguin walks or swims ...
# Is there a way to model situations like this where you want to reuse code
# for related objects but need different implementations for different objects
# while keeping the generality in the syntax

##### 1. Classes

# Blueprint for a student
class Student:
    """This is the blueprint for a student""" # docstring
    
    # constructor
    # NOTE: 'self' has to be stated explicitely
    # 'self' is like 'this' in C++/Java
    def __init__(self,n,a):
        
        # attributes are defined simply by using them
        self.name = n
        self.age = a

        print 'Hi, I am student %s. Thanks for creating me.' % self.name
    
    # a method
    # NOTE again: the first argument of a method must be 'self'
    # In principle you could call it diffenetly but 'self' is convention
    def get_age(self):
        return self.age

    def set_age(self, newage):
        self.age = newage

# Now that we have a blueprint for a student let's instantiate one:
bob = Student('Bob', 25)
# accessing an attribute
print 'Age of Bob:', bob.age

print "It's Bob's birthday"
# Calling a method
bob.set_age(26)
# Alternative way to call a method: 
print 'Age of Bob:', Student.get_age(bob)

##### 2. Private attributes and methods - Encapsulation

from datetime import datetime

class Student:
    """This is the blueprint for a student"""
    
    def __init__(self,n,a): 
        # The name of the student should not be changed after instanciation
        # therefore make it 'private' by adding '__' to name
        self.__name = n
        # Likewise for age
        self.__birthyear = datetime.now().year - a

        print 'Hi, I am student %s. Thanks for creating me.' % self.__name
    
        # NOTE: Real privacy doesn't exist in python
        # if 'bob' is an instance of Student '__name' can be accessed from
        # outside writing
        # >>> bob._Student__name 

    # a method
    # NOTE again: the first argument of a method must be 'self'
    # In principle you could call it diffenetly but 'self' is convention
    def get_age(self):
        return datetime.now().year - self.__birthyear

    # a special method, intended for 'pretty print' of the object
    # cf below for more special methods
    def __str__(self):
        return 'I am student %s and am %u years old.' % (self.__name, self.get_age())

# Now we execute the same code as above:
bob = Student('Bob', 25)

# NOTE: this doesn't work any more because we changed the implementation
# print 'Age of Bob:', bob.age 
# result would be: AttributeError: Student instance has no attribute 'age'

# But this still does:
print 'Age of Bob:', bob.get_age()

# Hence: it's generally a good idea to hide (make private) the internal 
# details of the implementation and provide access to the Class's functionality
# only through a defined interface

# And, by the way, accessing special method '__str__
print bob
str(bob)
bob.__str__()

###  NOTE: No need to free memory. Python has automatic garbage collection and will free an instance once it it's not referenced any more.
# Hence: no need for destructor

##### 3. Inheritance

# = extension of a class
class PhDStudent(Student):
    """A class representing a PhD student"""

    def __init__(self, n, a, gs):
        # Call parent class constructor
        Student.__init__(self, n, a)
        # Note: 'self.__init__(n,a)' not possible

        # adding a new attribute specific for a PhD student
        self.graduateSchool = gs

    # A new method
    def teach(self):
        print 'blablabla...'

    # Override a method
    def __str__(self):
        return 'I am Phd student %s and am %u years old. I am enrolled in the graduate school %s' % (self._Student__name, self.get_age(), self.graduateSchool)

sarah = PhDStudent('Sarah', 26, 'GGNB')
print sarah
print bob

sarah.teach()
#bob.teach() # -> AttributeError: Student instance has no attribute 'teach'

##### 4. More about attributes

### 4.1 Available attributes

# automatically generated attributes
sarah.__class__ # representing the class of sarah
#e.g.
if sarah.__class__ is int:
    print "What? Sarah is a number? You must be kidding."

sarah.__class__.__name__ # name of class
sarah.get_age.__name__ # name of method
Student.__doc__ # documentation string

# dictionary of attributes
sarah.__dict__

# list of names of all methods and attributes
dir(sarah)

# Checking if attribute exists
hasattr(sarah, 'teach') # -> True
hasattr(sarah, 'getBirthday') # -> False

### 4.2 Accessing attributes using strings of their names

# If name of an attribute of method is known only at runtime
# it can be accessed using 'getattr(object_instance, attribute_name), e.g.
getattr(sarah, 'graduateSchool')
getattr(sarah, 'teach')
getattr(sarah, 'teach')()
#getattr(sarah, 'getBirthday') # -> AttributeError, 'getBirthdat' doesn't exist

### 4.3 Dyanamically adding attributes

sarah.onHolidays = True
dir(sarah)

### 4.4 Class attributes (static attributes)

class counter:
    # class attribute / static attribute
    # NOTE: no 'self.'
    overall_total = 0
    
    def __init__(self):
        # data attribute
        self.my_total = 0

    def increment(self):
        counter.overall_total += 1
        self.my_total += 1
        
    def __str__(self):
        return 'total=%u\toverall_total=%u' % (self.my_total, counter.overall_total)

a=counter()
b=counter()
a.increment()
print a
print b
b.increment()
print a
print b
b.increment()
print a
print b

##### 5. Special methods

# We already encountered __init__ and __str__. But there are more like
# __cmp__: defines how comparison operators (<,<=,==,...) work
# __len__: defines result of 'len(object)'
# __add__: defines how to add objects
# ... many and more

# Example:

class Student:
    """This is the blueprint for a student"""
   
    def __init__(self,n,a): 
        self.__name = n
        self.__birthyear = datetime.now().year - a

        self.__cmpAttr = '_Student__name'

        print 'Hi, I am student %s. Thanks for creating me.' % self.__name

    def get_age(self):
        return datetime.now().year - self.__birthyear

    def __str__(self):
        return 'I am student %s and am %u years old.' % (self.__name, self.get_age())

    def iCareAboutAge(self):
        self.__cmpAttr = '_Student__birthyear'

    def __cmp__(self,rhs):
        lval = getattr(self,self.__cmpAttr)
        rval = getattr(rhs,self.__cmpAttr)

        if lval<rval:
            return -1
        elif lval==rval:
            return 0
        else:
            return 1
        
bob = Student('bob', 25)
joe = Student('joe', 27)
print bob<joe
bob.iCareAboutAge()
print bob<joe

##### References

# The talk relied on a course given in spring 2008 at the University of Pennsylvania
# www.cis.upenn.edu/~cis530/slides-2008/Python-complete-tutorial-2008-spring.ppt

# Hans Petter Langtangen. Python Scripting for Computational Science.
