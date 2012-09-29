from numpy import *
import matplotlib.pyplot as plt

class IFNeuron:
    """Integrate-and-fire neuron"""

    def __init__(self, cm=1, gL=0.01 , EL=-55, Vthreshold=0, Vreset=-70, V0=-60, stepSize = 0.1):
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
        self.tau = float(self.cm)/self.gL
        self.Vinf = self.EL + float(self.Iext)/self.gL

    def setIext(self, Iext):
        self.Iext = Iext
        self.__calcODEConsts()

    def __step(self):
        Vdot = float(-self.Vtrace[-1]+self.Vinf)/self.tau
        V = self.Vtrace[-1] + self.stepSize * Vdot #explicit Euler method
        self.Vtrace.append(V)

        if V>=self.Vthreshold:
            self.__fire()

    def __fire(self):
        self.Vtrace[-1] = self.Vreset
        #record spike?

    def run(self, T):
        t=0
        while t<T:
            self.__step()
            t += self.stepSize

    def plot(self):
        plt.plot(self.Vtrace)
        plt.show()
        
def test_ifneuron():
    n = IFNeuron()
    n.setIext(1)
    n.run(1000)
    n.plot()

if __name__=='__main__':
    test_ifneuron()
