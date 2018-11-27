# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:01:53 2014

@author: JF
"""
import matplotlib.gridspec as gridspec
from pylab import *
# Used for arbitrary subplots, with possible aliasing between them and all that      
    
    
def plot_sighisto(X,M=10,fig=None):
    figure(fig); clf()
    G = gridspec.GridSpec(12, 12)
    ax1 = subplot(G[0:8, 0:12])
    ax2 = subplot(G[9:12, 0:12],sharex=ax1)
    #G.update(left=0.05, right=0.48, wspace=0.05)
    N=len(X)
    D=max(X)-min(X) 
    ax1.plot(X,range(N))
    ax1.set_ylabel('Time')
    ax1.axis([min(X)-D/10, max(X)+D/10, 0, N])
    # make these tick labels invisible
    setp( ax1.get_xticklabels(), visible=False)
    (n,b,p)=plt.hist(X,M)
    ax2.hist(X,M)
    ax2.set_xlabel('Amplitude')  
    ax2.set_ylim([0, 1.1*max(n)])
    #ax2.axis([min(X)-D/10, max(X)+D/10, 0, 1.1*max(h)])
    # Reset the bottom subplot to have xticks
    #setp(gca,'xtickMode', 'auto')


if __name__ == '__main__':
        import scipy.stats as stats
        import matplotlib.gridspec as gridspec
# Used for arbitrary subplots, with possible aliasing between them and all that      
        rv=stats.norm(loc=0,scale=1) 
        plot_sighisto(rv.rvs(200),fig=2)