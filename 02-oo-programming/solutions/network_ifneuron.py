from numpy import *
import matplotlib.pyplot as plt

class IFNeuron:
    """Integrate-and-fire neuron
       =========================
       This version of IFNeuron is, essentially, idential to the one
       in file 'ifneuron.py'. Only some details changed that were necessary
       or convenient if the neuron is supposed to be part of a network of 
       neurons.
    """

    def __init__(self, 
                 neuronID,
                 network,
                 cm=1, 
                 gL=0.01 , 
                 EL=-55, 
                 Vthreshold=0, 
                 Vreset=-70, 
                 V0=-60, 
                 stepSize = 0.1,
                 ):

        # These are new in the network version
        self.__neuronID = neuronID
        self.__network = network

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
        # For convenience, store these combinations of the variables
        # because it's exactly these combinations that occur in the
        # step(self) function
        self.tau = float(self.cm)/self.gL
        self.Vinf = self.EL + float(self.Iext)/self.gL

    def setIext(self, Iext):
        """ Set external current impinging on this neuron. """
        self.Iext = Iext
        self.__calcODEConsts()

    def step(self):
        """ Evolve voltage of this neuron by one time step. 
        Compared to the non-network version, it is now a public function,
        because it is supposed to be called by the network, that is: from
        outside the neuron.
        """
        Vdot = float(-self.Vtrace[-1]+self.Vinf)/self.tau
        V = self.Vtrace[-1] + self.stepSize * Vdot #explicit Euler method
        self.Vtrace.append(V)

        # The part checking for a spike is now a separate function

    def checkForSpike(self):
        """ If voltage crosses threshold, then fire """
        if self.Vtrace[-1]>=self.Vthreshold:
            self.__fire()

    def __fire(self):
        """ If this neuron fires, send a spike to all connected neurons,
            that is, send a spike causing a psp to all neurons, only if
            psp != 0 this has an effect """
        self.Vtrace.append(self.Vreset)
        for i in xrange(self.__network.nNeurons()):
            psp = self.__network.psp(i,self.__neuronID)
            self.__network.neuron(i).receiveSpike(psp)

    def receiveSpike(self,psp):
        """ The effect of receiving a spike is to change the voltage of
            this neuron by an amount psp
        """
        self.Vtrace[-1] += psp

    def plot(self):
        """ Plot voltage trace """
        plt.plot(self.Vtrace)
        plt.show()
