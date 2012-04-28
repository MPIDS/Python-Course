import scipy.io as io

def load1():
    """Call: '(I,FI,TimeResolutionS,SamplingFrequencyHz) = load2()'
    The variables I,FI,TimeResolutionS,SamplingFrequencyHz are those
    defined in the task description on the exercise sheet.
    """
    
    data = io.loadmat('data_spontaneous_recording.mat')
    
    I=data['data']['I'][0][0].ravel()
    FI=data['data']['FI'][0][0].ravel()
    TimeResolutionS=data['data']['TimeResolutionS'][0][0][0][0]
    SamplingFrequencyHz=data['data']['SamplingFrequencyHz'][0][0][0][0]
    
    return I,FI,TimeResolutionS,SamplingFrequencyHz


def load2():
    """Call: '(I,Z,I_SamplingFrequencyHz,Z_SamplingFrequencyHz) = load2()'
    The variables I,Z,I_SamplingFrequencyHz,Z_SamplingFrequencyHz are those
    defined in the task description on the exercise sheet.
    """

    data = io.loadmat('data_synaptic_response_variability.mat')
    
    I=data['data']['I'][0][0].ravel()
    Z=data['data']['Z'][0][0].ravel()
    I_SamplingFrequencyHz=data['data']['I_SamplingFrequencyHz'][0][0][0][0]
    Z_SamplingFrequencyHz=data['data']['Z_SamplingFrequencyHz'][0][0][0][0]
    
    return I,Z,I_SamplingFrequencyHz,Z_SamplingFrequencyHz
