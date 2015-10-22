import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def plt_LPtemplate(omega, A, Abounds=None):
    """omega contains the template frequencies [band-pass, band-stop]
       A contains the corersponding attenuations, Abounds, the y limits for the display 
    """
    [omegac, omegaa]=omega
    [Ac, Aa]=A
    if Abounds is None:
        delta=np.max(A)-np.min(A); Amax=np.max(A)+delta/5; Amin=np.min(A)-delta/5
    else:
        [Amax, Amin]=(Abounds)
    plt.plot([-omegac, -omegac, omegac, omegac],[Amin, Ac, Ac, Amin],'-', color='blue')
    plt.fill_between([-omegac, -omegac, omegac, omegac],[Amin, Ac, Ac, Amin], Amin, 
                     color='lightblue', alpha=0.6)
    
    plt.plot([-pi, -omegaa, -omegaa],[Aa, Aa, Amax],'-', color='blue')
    plt.fill_between([-pi, -omegaa, -omegaa],Amax, [Aa, Aa, Amax], color='lightblue', alpha=0.6)
    plt.plot([omegaa, omegaa,pi],[Amax, Aa, Aa],'-', color='blue')
    plt.fill_between([omegaa, omegaa,pi],Amax, [Amax, Aa, Aa],color='lightblue', alpha=0.6)
    plt.ylim([Amin, Amax])
    plt.xlim([-pi, pi])
    
    #plt.text(-3.7,0.4,'Fs/2', color='blue',fontsize=14)
if __name__=="__main__":
    plt_LPtemplate([1, 1.84],[0, -20],Abounds=[5, -35])