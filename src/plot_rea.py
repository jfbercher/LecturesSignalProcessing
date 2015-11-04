# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:51:59 2014

@author: JF
"""
def plot_rea(sig,nb=10,fig=None):
    """
    Plot  `nb` realizations of the random variable object `rv`
    
    Parameters
    ----------
    rv:  object       
        the random variable array
    nb:  number
        number of realizations to display
    Returns
    -------
    Nothing
    Modules
    -------
    import matplotlib.gridspec as gridspec
    from itertools import cycle
    
    Examples
    --------
    >>> rv=stats.norm(loc=0,scale=1) 
    >>> plot_rea()
            
    """
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    from itertools import cycle
    
    plt.figure(fig); plt.clf()
    plt.suptitle("Realizations and means of a random signal",fontsize=14,color='blue')
    G = gridspec.GridSpec(12, 12)
    #fig=figure(figsize=(10,4))
    ax1 = plt.subplot(G[0:9, 0:10])
    ax2 = plt.subplot(G[10:12, 0:10])
    ax3 = plt.subplot(G[0:9, 11:12])
    
    
    (K,N)=np.shape(sig)
    sig_sampled=sig[np.random.randint(0,K,nb),:]
    deltaA=sig.max()-sig.min()
    yrea=deltaA*np.linspace(0,nb,nb)
    decalage=np.outer(yrea,np.ones(N))
    sig_sampled_dec=sig_sampled+0.5*decalage
        
    ax1.xaxis.tick_top()
    ax1.plot(sig_sampled_dec.T)
    ax1.set_yticks(yrea/2)#,
    ax1.set_yticklabels([str(x) for x in list(range(1,nb+1))])
    ax1.set_xlim([0,N])
    fivepercent=(sig_sampled_dec.max()-sig_sampled_dec.min())/20
    ax1.set_ylim([sig_sampled_dec.min()-fivepercent, sig_sampled_dec.max()+fivepercent])
    ax1.set_ylabel("Realizations",fontsize=14)

    msig0=np.mean(sig,axis=0)      
    ax2.plot(msig0)
    ax2.set_xlim([0,N])
    ax2.set_xlabel("Time",fontsize=14)
    ax2.annotate("Ensemble average",
                 xy=(80,msig0[80]), 
                 xytext=(0.55,0.25), textcoords='figure fraction'
#                 ,
#         arrowprops=dict(arrowstyle="->",
#                         color="green",
#                         connectionstyle="arc3,rad=0.3",
#         shrinkA=10, shrinkB=10)
         )
   # yticks([])
    
    clist = plt.rcParams['axes.color_cycle']
    colorcycler = cycle(clist)
    ax3.yaxis.tick_right()
    m_sig_sampled1=np.mean(sig_sampled,axis=1)
    for k in range(len(yrea)):
        ax3.plot(m_sig_sampled1[k],yrea[k]/2,'o', color=next(colorcycler)) #sig
    ax3.plot(np.mean(sig_sampled,axis=1),yrea/2, alpha=0.5) #sig
    ax3.set_ylim([sig_sampled_dec.min()-fivepercent, sig_sampled_dec.max()+fivepercent])
    ax3.set_yticks(yrea/2)#,
    ax3.set_yticklabels([str(x) for x in list(range(1,nb+1))])
    ax3.set_xticks([m_sig_sampled1.min(), m_sig_sampled1.max()])
    ax3.set_xticklabels(["{0:2.2f}".format(m_sig_sampled1.min()), "{0:2.3f}".format(m_sig_sampled1.max())])#,
    ax3.annotate("Time \naverage",
                 xy=(m_sig_sampled1[0],yrea[0]/2), #xycoords='figure fraction',
                 xytext=(0.85,0.92), textcoords='figure fraction'
                 #,
#         arrowprops=dict(arrowstyle="->",
#                         color="blue",
#                         connectionstyle="arc3,rad=0.3",
#         shrinkA=10, shrinkB=10)
         )
    #ax3.set_xlim([0,N])

    
if __name__ == '__main__':
        import scipy.stats as stats
        import matplotlib.gridspec as gridspec
        from itertools import cycle
# Used for arbitrary subplots, with possible aliasing between them and all that      
    
        rv=stats.norm(loc=0,scale=1) 
        size=(100,150)
        sig=rv.rvs(size=size)
        plot_rea(sig,nb=10,fig=1)
