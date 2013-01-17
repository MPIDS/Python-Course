from numpy import *
import matplotlib.pyplot as plt

class IFNeuron:
    """Integrate-and-fire neuron"""

    def __init__(self, cm=1, gL=0.01 , EL=-55, Vthreshold=0, Vreset=-70, V0=-60, stepSize = 0.1):
        # Make local copies of all parameters
        # For simplicity, they are all public variables
        # In a more 'restrictive' version, I would make them private
        # (i.e. replace self.cm by self.__cm and likewise for the others)
        # and provide functions to access and, maybe, change them
        self.cm = cm
        self.gL = gL
        self.EL = EL
        self.Vthreshold = Vthreshold
        self.Vreset = Vreset
        self.Vtrace = [V0]
        self.stepSize = stepSize

        self.Iext = 0.0
        
        self.__calcODEConsts()
        
        
    def __calcODEConsts(self):
        # These constants are needed in the __step function
        self.tau = float(self.cm)/self.gL
        self.Vinf = self.EL + float(self.Iext)/self.gL

    def setIext(self, Iext):
        """ Set external current received by neuron """
        self.Iext = Iext
        # as self.tau and self.Vinf depend on Iext, they have to be
        # recalculated
        self.__calcODEConsts()

    def __step(self):
        # Evolves membrane potential of this neuron by one timestep
        Vdot = float(-self.Vtrace[-1]+self.Vinf)/self.tau
        V = self.Vtrace[-1] + self.stepSize * Vdot #explicit Euler method
        self.Vtrace.append(V)

        # If membrane potential crosses threshold: fire!
        if V>=self.Vthreshold:
            self.__fire()

    def __fire(self):
        # For an integrate-and-fire neuron, firing only means to reset 
        # the voltage
        self.Vtrace[-1] = self.Vreset
        # One could, in principal, also record the time of the spike

    def run(self, T):
        """ Evolve the neuron for a time T """
        t=0
        while t<T:
            self.__step()
            t += self.stepSize

    def plot(self):
        """ Plot voltage trace as far as it has been simulated already """
        plt.plot(self.Vtrace)
        plt.show()
        
def test_ifneuron():
    n = IFNeuron()
    n.setIext(1)
    n.run(1000)
    n.plot()

if __name__=='__main__':
    test_ifneuron()
