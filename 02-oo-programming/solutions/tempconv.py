## Source: {{{ http://code.activestate.com/recipes/286226/ (r2)
class Temperature(object):
    equations = {'c': (1.0, 0.0, -273.15), 'f': (1.8, -273.15, 32.0),
                 'r': (1.8, 0.0, 0.0)}

    def __init__(self, k=0.0, **kwargs):
        """ Allow the temperature instance to be created as:
        temp = Temperature() # to initialize with 0 Kelvin
        temp = Temperature(k=x) # to initialize with x Kelvin
        temp = Temperature(c=x) # to initialize with x Celsius
        temp = Temperature(f=x) # to initialize with x Fahrenheit
        """
        self.k = k
        for k in kwargs:
            if k in ('c', 'f', 'r'):
                setattr(self, k, kwargs[k])
                break

    def __getattr__(self, name):
        """ Let temp be an instance of this Temperature class.
        This function allows to access the temperature values in all units
        (K,C,F) using dot-notation. I.e. temp.k returns temperature in Kelvin,
        temp.c in Celsius and temp.f in Fahrenheit
        """
        if name in self.equations:
            eq = self.equations[name]
            return (self.k + eq[1]) * eq[0] + eq[2]
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        """ Similar to __getattr__, but this function allows to set
        temperatures using dot-notation, for example: 
        temp.k=10 to set temperature to 10K.
        """
        if name in self.equations:
            eq = self.equations[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return "%g K" % self.k

    def __repr__(self):
        return "Temperature(%g)" % self.k
## end of http://code.activestate.com/recipes/286226/ }}}

def test_tempconv():
    print "Setting temperature to 10K"
    temp = Temperature(k=10)
    print temp.k, 'K =', temp.c, 'C =', temp.f, 'F'

    print "Setting temperature to 5C"
    temp.c = 5
    print temp.k, 'K =', temp.c, 'C =', temp.f, 'F'

if __name__=='__main__':
    test_tempconv()
