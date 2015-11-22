import numpy as np
from zerospolesdisplay import *

poles=np.array([0])
zeros=np.array([0.95*np.exp(1j*2*pi*0.4)])
A=ZerosPolesDisplay(poles,zeros)

