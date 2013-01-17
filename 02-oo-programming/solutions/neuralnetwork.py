import numpy as np
from network_ifneuron import IFNeuron
from random import random

class NeuralNetwork:
    """Neural network class
       ====================
    """

    def __init__(self, nNeurons):

        self.__nNeurons = nNeurons

        self.__neurons = []
        for i in xrange(nNeurons):
            n = IFNeuron(i,self)
            n.setIext(1)
            self.__neurons.append(n)
 
        # connectionMatrix is a matrix of size nNeurons x nNeurons
        # Its entries c_{ij} give the post-synaptic-potential neuron i
        # receives if neuron j spikes.
        # I.e. neuron j has a synapse on neuron i if and only if
        # c_{ij} != 0
        # Technical note: I use a numpy array to store the matrix,
        # but in principle one could also use a list of lists
        self.__connectionMatrix = np.zeros( (nNeurons,nNeurons) )
        
        # interconnect neurons with probability 0.25
        self.__connectNeurons(0.25)

    def __connectNeurons(self,p):
        """ Connect all neurons in network to all others with probability p
            For simplicity assume that all PSPs are the same
        """

        psp = 1

        for i in xrange(self.__nNeurons):
            for j in xrange(self.__nNeurons):
                if random()<p:
                    self.__connectionMatrix[i,j] = psp
                    
    def nNeurons(self):
        """ Returns the number of neurons in the network """
        return self.__nNeurons

    def psp(self,i,j):
        """ Returns the postsynaptic-potential in neuron i when receiving 
            a spike from neuron j
        """
        return self.__connectionMatrix[i,j]

    def neuron(self,i):
        """ Return neuron number i in the network """
        return self.__neurons[i]

    def simulate(self,nTimesteps):
        """ Run the simulation for nTimesteps steps """

        for i in xrange(nTimesteps):
            # first, evolve voltage
            for n in self.__neurons:
                n.step()

            # then, check which neuron spiked and, if so, transmit spikes
            for n in self.__neurons:
                n.checkForSpike()

def test_network():
    nn = NeuralNetwork(100)
    nn.simulate(10000)
    nn.neuron(0).plot()
    nn.neuron(1).plot()

if __name__=='__main__':
    test_network()
