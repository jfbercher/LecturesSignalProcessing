"""
Zeros/Poles + impulse response  + transfer function displays 
jfb 2015 - last update november 22, 2015
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


#line, = ax.plot(xs, ys, 'o', picker=5)  # 5 points tolerance

class ZerosPolesDisplay():
    
  def __init__(self,poles=np.array([0.7*np.exp(1j*2*np.pi*0.1)]),
               zeros=np.array([1.27*np.exp(1j*2*np.pi*0.3)]),
               N=1000, response_real=True, ymax=1.2, Nir=64):
               
    
    self.poles=poles
    self.zeros=zeros
        
    self.ymax=np.max([ymax, 1.2*np.max(np.concatenate((np.abs(poles), np.abs(zeros))))])
    self.poles_th=np.angle(self.poles)
    self.poles_r=np.abs(self.poles)
    self.zeros_th=np.angle(self.zeros)
    self.zeros_r=np.abs(self.zeros)
    self.N=N
    self.Nir=Nir
    
    self.poles_line = None
    self.zeros_line = None
    self.setup_main_screen()


    
  def setup_main_screen(self):
        
    import matplotlib.gridspec as gridspec
    
    #Poles & zeros
    self.fig = plt.figure(figsize=(9,7))
    gs = gridspec.GridSpec(3,12) 
    #self.ax = self.fig.add_axes([0.1, 0.1, 0.77, 0.77], polar=True, axisbg='#d5de9c')
    #self.ax=self.fig.add_subplot(221,polar=True, axisbg='#d5de9c')
    self.ax = plt.subplot(gs[0:,0:6],polar=True,axisbg='#d5de9c')
    #self.ax = self.fig.add_subplot(111, polar=True)
    self.fig.suptitle('Poles & zeros adjustment',fontsize=18, color='blue', 
                      x=0.1, y=0.98, horizontalalignment='left')
    #self.ax.set_title('Poles & zeros adjustment',fontsize=16, color='blue')
    self.ax.set_ylim([0, self.ymax])
    self.poles_line, = self.ax.plot(self.poles_th,self.poles_r,'ob',ms=9, picker=5, label="Poles")
    self.zeros_line, = self.ax.plot(self.zeros_th,self.zeros_r,'Dr',ms=9, picker=5, label="Zeros")
    self.ax.plot(np.linspace(-np.pi,np.pi,500),np.ones(500),'--b',lw=1)
    self.ax.legend()
    
               
    #Transfer function
    self.axTF0= plt.subplot(gs[0,6:11],axisbg='LightYellow')
    #self.axTF[0].set_axis_bgcolor('LightYellow')
    self.axTF0.set_title('Transfer function (modulus)')
    #self.axTF1=self.fig.add_subplot(224,axisbg='LightYellow')
    self.axTF1=plt.subplot(gs[1,6:11],axisbg='LightYellow')
    self.axTF1.set_title('Transfer function (phase)')
    self.axTF1.set_xlabel('Frequency')
    f=np.linspace(0,1,self.N)
    self.TF=np.fft.fft(np.poly(self.zeros),self.N)/np.fft.fft(np.poly(self.poles),self.N)
    self.TF_m_line, = self.axTF0.plot(f,np.abs(self.TF))
    self.TF_p_line, = self.axTF1.plot(f,180/np.pi*np.angle(self.TF))
    #self.figTF.canvas.draw()
    
    #Impulse response
    #self.figIR = plt.figure()
    #self.axIR = self.fig.add_subplot(223,axisbg='Lavender')
    self.axIR =  plt.subplot(gs[2,6:11],axisbg='Lavender')
    self.IR= np.real(self.impz(self.zeros,self.poles,self.Nir)) #np.real(np.fft.ifft(self.TF))
    self.axIR.set_title('Impulse response')
    self.axIR.set_xlabel('Time')
    self.IR_m_line, = self.axIR.plot(self.IR)
    #self.figIR.canvas.draw()        
    self.fig.canvas.draw()
    self.fig.tight_layout()    
 
  def impz(self,zeros,poles,L):
        from scipy.signal import lfilter
        a=np.poly(poles)
        b=np.poly(zeros)
        d=np.zeros(L)
        d[0]=1
        h=lfilter(b,a,d)
        return h
    

if __name__=="__main__":    
    #sym_comp([1+1j, 2, 3-2j])
    #case of complex poles and zeros
    poles=np.array([0.8*np.exp(1j*2*pi*0.125), 0.8*np.exp(1j*2*pi*0.15), 0.5])
    zeros=np.array([0.95*np.exp(1j*2*pi*0.175), 1.4*np.exp(1j*2*pi*0.3), 0])
    A=ZerosPolesDisplay(poles,zeros)

    """
    #case of a single real pole
    poles=np.array([0.5])
    zeros=np.array([0])
    A=ZerosPolesPlay(poles,zeros,response_real=False)
    """

    #plt.show()
