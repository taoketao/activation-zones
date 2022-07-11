# Python 3.5.4
import numpy as np
import matplotlib.pyplot as plt

'''     p=z: x/(1+|x|^z)^(1/z).    Gudder(mann): arctan(tanh(x))*4/pi.
        exp*: {x>0: 1-e^-x.  x<=0: e^x-1.}
        name        alpha  beta   gamma  delta     '''
d = {\
        'tanh':    [0.421, 0.658, 1.146, 1.572],\
        'erf':     [0.488, 0.620, 1.076, 1.456],\
        'p=2':     [0.325, 0.577, 1.000, 1.376],\
        'exp*':    [0.001, 0.693, 1.386, 2.079],\
        'arctan':  [0.379, 0.765, 1.330, 1.847],\
        'Gudder':  [0.284, 0.496, 0.877, 1.228],\
        'p=1':     [0.001, 0.500, 1.000, 1.500],\
        'p=1.5':   [0.161, 0.543, 1.000, 1.432],\
        'p=4.37':  [0.680, 0.681, 1.000, 1.228],\
        'x-x^2*':  [0.000, 0.845, 2.000, None ],\
        'xrootx*': [0.249, 0.306, 0.426, 0.538],\
        'relu':    [0, 0,0,0],\
    }
titles_ordered=['tanh'  ,'erf'  ,'p=2'  ,'exp*'  ,'arctan'  ,'Gudder'  ,'p=1'  ,'p=1.5'  ,'p=4.37', 'relu' ][::-1]
colors_ = ['blue', 'cyan', 'lightseagreen', 'blueviolet', 'violet', 'mediumvioletred', 'peru', 'coral', 'tomato', 'black'][::-1]

A = np.array( [ d[title] for title in titles_ordered] ).T
l=len(d)
diff = np.array( [ [i*.5]*l for i in range(4) ] )  # rotate plots
handles=[]
for i in list(range(l)): 
#    h, = plt.plot(list(range(4)), A[:,i]-diff[:,i], '-o',
    if titles_ordered[i]=='relu':
        plt.annotate(r'Linear or Relu or LeakyRelu are degenerate; nonzero weights act the same everywhere. $\alpha$/$\beta$/$\gamma$/$\delta$'+\
                ' and are not meaningful.', \
                (0.03, i-.1), fontsize=6) 
        h, = plt.plot( [0], [i], '-o', color=colors_[i], label=titles_ordered[i])
        handles =[h]+handles
        continue
    h, = plt.plot( A[:,i], [i]*4, 
         '-o', color=colors_[i], label=titles_ordered[i])
    handles =[h]+handles
    for j in range(4):
#        plt.annotate('abcd'[j], (A[j,i]-0.02, i+0.15), fontsize=6) 
        plt.annotate([r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$'][j], \
                (A[j,i]-0.02, i+0.15), fontsize=6) 

plt.yticks(range(l),titles_ordered)

plt.legend(handles=handles, bbox_to_anchor=(1.,.5), loc='center left') # , mode='expand') 
plt.tight_layout(rect=[0,0.05,0.85,0.8])
plt.xticks([0,0.5,1,1.5,2,2.5])
plt.title('** version: alternative presentation for more easily picturing zones. **\n'+\
        'Analyzing zone-determining special points of the upper half of sigmoidal activation functions. \n'+\
    'Define D2 := d/dt w_ij = (y_i-sigm(v_i))*(d/dv_i sigm(v_i))*x_j, where v_i = w_i.dot(x).  \n'+\
    '(D2 is named so because for some sigmoids, D2 = d^2/dt^2 sigm().) Define D4 := d^2/dw^2 (D2). \n'+\
    'alpha: the place where curvature (=|D4|) is maximal, corresponding to weights most sensitive to training noise.\n'+\
    'beta: the peak of D2, where weights change the most per signal and is an unstable equilibrium.\n'+\
    'gamma: D4 crosses zero and D2 is linear; this is a region where weights are robust against training noise.\n'+\
    "delta: a distal local peak/trough of D4 where weights are unusually sensitive to noise. Beyond it, weights are 'lost'.\n"+\
    "Parameters: y_i=0, w_i.dot(x)=1, x_j=1. ('training noise': any source of variability that makes weights walk up and down. \n"+\
    'e.g. batch learning, imperfect data, numerical artifacts of learning rate, or interdependence of weights on each other.)\n'+\
    '', fontdict={'fontsize':8})

#print(' raw data: '+str(d))
data_as_str = 'raw data: '+', '.join([v+':'+str(k) for v,k in d.items() if v in titles_ordered[:3] ])\
        +',\n'+ ', '.join([v+':'+str(k)+',  ' for v,k in d.items() if v in titles_ordered[3:6] ])\
        +',\n'+ ', '.join([v+':'+str(k)+',  ' for v,k in d.items() if v in titles_ordered[6:] ])
# plt.text(0.95, 0.1, ' raw data: '+data_as_str, va="bottom", ha, fontsize=6)
plt.annotate( data_as_str, (0,0), (0,-20), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=6) # https://stackoverflow.com/questions/7917107/add-footnote-under-the-x-axis-using-matplotlib


plt.show()
plt.close()
