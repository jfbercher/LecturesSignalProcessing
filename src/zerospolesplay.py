"""
Transfer function adjustment using zeros and poles drag and drop!
jfb 2015 - last update january 08, 2015
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


#line, = ax.plot(xs, ys, 'o', picker=5)  # 5 points tolerance

class ZerosPolesPlay():
    
  def __init__(self,poles=np.array([0.7*np.exp(1j*2*np.pi*0.1)]),
               zeros=np.array([1.27*np.exp(1j*2*np.pi*0.3)]),
               N=1000, response_real=True, ymax=1.2, Nir=64):
               
    if response_real:
        self.poles, self.poles_isreal = self.sym_comp(poles)
        self.zeros, self.zeros_isreal = self.sym_comp(zeros)
    else:    
        self.poles=poles
        self.poles_isreal= (np.abs(np.imag(poles))<1e-12)
        self.zeros=zeros
        self.zeros_isreal =(np.abs(np.imag(zeros))<1e-12)
    
    self.ymax=np.max([ymax, 1.2*np.max(np.concatenate((np.abs(poles), np.abs(zeros))))])
    self.poles_th=np.angle(self.poles)
    self.poles_r=np.abs(self.poles)
    self.zeros_th=np.angle(self.zeros)
    self.zeros_r=np.abs(self.zeros)
    self.N=N
    self.Nir=Nir
    self.response_real=response_real
    
    self.being_dragged = None
    self.nature_dragged = None
    self.poles_line = None
    self.zeros_line = None
    self.setup_main_screen()
    self.connect()
    self.update()

    
  def setup_main_screen(self):
        
    import matplotlib.gridspec as gridspec
    
    #Poles & zeros
    self.fig = plt.figure()
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
    self.ax.legend(loc=1)
    
               
    #Transfer function
    #self.figTF, self.axTF = plt.subplots(2, sharex=True)
    #self.axTF0=self.fig.add_subplot(222,axisbg='LightYellow')
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
    self.IR= self.impz(self.zeros,self.poles,self.Nir) #np.real(np.fft.ifft(self.TF))
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
    
  def sym_comp(self,p):
    L=np.size(p)
    r=list()
    c=list()
    for z in p: 
        if np.abs(np.imag(z))<1e-12: 
            r.append(z)
        else:
            c.append(z)
    out=np.concatenate((c,r,np.conjugate(c[::-1])))           
    isreal=(np.abs(np.imag(out))<1e-12)       
    return out,isreal
#sym_comp([1+1j, 2, 3-2j])

  def connect(self):
    self.cidpick = self.fig.canvas.mpl_connect(
      'pick_event', self.on_pick)
    self.cidrelease = self.fig.canvas.mpl_connect(
      'button_release_event', self.on_release)
    self.cidmotion = self.fig.canvas.mpl_connect(
      'motion_notify_event', self.on_motion)

  def update(self):  
        
    #poles and zeros
    #self.fig.canvas.draw()
    
    #Transfer function & Impulse response
    if not(self.being_dragged is None): 
        #print("Was released")

        f=np.linspace(0,1,self.N)
        self.TF=np.fft.fft(np.poly(self.zeros),self.N)/np.fft.fft(np.poly(self.poles),self.N)
        self.TF_m_line.set_ydata(np.abs(self.TF))
        M=np.max(np.abs(self.TF))
        #update the yscale
        current_ylim=self.axTF0.get_ylim()[1]
        if M>current_ylim or M<0.5*current_ylim: self.axTF0.set_ylim([0, 1.2*M])

        #phase
        self.TF_p_line.set_ydata(180/np.pi*np.angle(self.TF))
        #self.figTF.canvas.draw()
        
        # Impulse response
        self.IR=self.impz(self.zeros,self.poles,self.Nir) #np.fft.ifft(self.TF)
        #print(self.IR)
        self.IR_m_line.set_ydata(self.IR)
        M=np.max(self.IR)
        Mm=np.min(self.IR)
        #update the yscale
        current_ylim=self.axIR.get_ylim()
        update_ylim=False
        if M>current_ylim[1] or M<0.5*current_ylim[1]: update_ylim=True 
        if Mm<current_ylim[0] or np.abs(Mm)>0.5*np.abs(current_ylim[0]): update_ylim=True     
        if update_ylim: self.axIR.set_ylim([Mm, 1.2*M])
        
        #self.figIR.canvas.draw()
    self.fig.canvas.draw() 
    
    
  def on_pick(self, event):
    """When we click on the figure and hit either the line or the menu items this gets called."""
    if event.artist != self.poles_line and event.artist != self.zeros_line: 
         return
    self.being_dragged = event.ind[0]
    self.nature_dragged = event.artist


  def on_motion(self, event):
    """Move the selected points and update the graphs."""
    if event.inaxes != self.ax: return
    if self.being_dragged is None: return
    p = self.being_dragged #index of points on the line being dragged
    xd = event.xdata
    yd = event.ydata
    #print(yd)
    if self.nature_dragged==self.poles_line: 
        x,y = self.poles_line.get_data()
        if not (self.poles_isreal[p]):
            x[p],y[p]=xd,yd
        else:
            if np.pi/2<xd<3*np.pi/2:
                x[p],y[p]=np.pi,yd
            else:
                x[p],y[p]=0,yd  
        x[-p-1],y[-p-1]=-x[p],y[p]        
        self.poles_line.set_data(x,y) # then update the line
        #print(self.poles)
        self.poles[p]=y[p]*np.exp(1j*x[p])  
        self.poles[-p-1]=y[p]*np.exp(-1j*x[p])
        
    else:
        x,y = self.zeros_line.get_data()   
        if not (self.zeros_isreal[p]):
            x[p],y[p]=xd,yd
        else:
            if np.pi/2<xd<3*np.pi/2:
                x[p],y[p]=np.pi,yd
            else:
                x[p],y[p]=0,yd    
        x[-p-1],y[-p-1]=-x[p],y[p] 
        self.zeros_line.set_data(x,y) # then update the line
        self.zeros[p]=y[p]*np.exp(1j*x[p]) # then update the line
        self.zeros[-p-1]=y[p]*np.exp(-1j*x[p])    
 
    
    self.update() #and the plot

  def on_release(self, event):
    """When we release the mouse, if we were dragging a point, recompute everything."""
    if self.being_dragged is None: return

    self.being_dragged = None
    self.nature_dragged= None
    self.update()


#case of complex poles and zeros
poles=np.array([0.8*np.exp(1j*2*pi*0.125), 0.8*np.exp(1j*2*pi*0.15), 0.5])
zeros=np.array([0.95*np.exp(1j*2*pi*0.175), 1.4*np.exp(1j*2*pi*0.3), 0])
A=ZerosPolesPlay(poles,zeros)

"""
#case of a single real pole
poles=np.array([0.5])
zeros=np.array([0])
A=ZerosPolesPlay(poles,zeros,response_real=False)
"""

plt.show()


#At the end, poles and zeros available as A.poles and A.zeros