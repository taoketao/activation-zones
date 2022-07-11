# Python 3.5.4
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
fig.set_size_inches((8, 5))

'''         name        alpha  beta   gamma  delta     '''
dl = []  # to become dict; but want ordered keys first
dl.append( {'tanh':    [0.421, 0.658, 1.146, 1.572] } )
dl.append( {'erf':     [0.488, 0.620, 1.076, 1.456] } )
dl.append( {'p=2':     [0.325, 0.577, 1.000, 1.376] } )
dl.append( {'exp*':    [0.001, 0.693, 1.386, 2.079] } )
dl.append( {'arctan':  [0.379, 0.765, 1.330, 1.847] } )
dl.append( {'Gudder':  [0.284, 0.496, 0.877, 1.228] } )
dl.append( {'p=1':     [0.001, 0.500, 1.000, 1.500] } )
dl.append( {'p=1.5':   [0.161, 0.543, 1.000, 1.432] } )
dl.append( {'p=4.37':  [0.680, 0.681, 1.000, 1.228] } )
dl.append( {'x-x^2*':  [0.000, 0.845, 2.000, None ] } )
dl.append( {'xrootx*': [0.676, 0.832, 1.158, 1.462] } ) #  another alpha/delta at 0.383
dl.append( {'xrootx2': [0.298, 0.561, 1.000, 1.419] } )
dl.append( {'relu':    [0    , 0    , 0    , 0    ] } )
# Changing the above? Remember to add the data to commentary_figures.txt!

titles_ordered= [ list(dl_entry.keys())[0] for dl_entry in dl ][::-1]
d = {}
for dl_entry in dl:
    d.update(dl_entry)
#colors_ = ['blue', 'cyan', 'lightseagreen', 'blueviolet', 'violet',
#           'mediumvioletred', 'peru', 'coral', 'tomato', 'black'][::-1]
colors_ = ['blue', 'cyan', 'lightseagreen', 'blueviolet', 'violet', 'mediumvioletred',
           'lightseagreen','lightseagreen', 'lightseagreen', 'coral', 'peru', 'maroon',
           'gray'][::-1]
if not len(colors_) == len(d):
    raise("please add more/less colors "+','.join([len(colors_), len(d)]))

A = np.array( [ d[title] for title in titles_ordered] ).T
l=len(d)
diff = np.array( [ [i*.5]*l for i in range(4) ] )  # rotate plots
handles=[]
for i in list(range(l)): 
#    h, = plt.plot(list(range(4)), A[:,i]-diff[:,i], '-o',
    sigm_id = titles_ordered[i]
    if sigm_id=='relu':
        plt.annotate(r'Linear, Relu, LeakyRelu, HardTanh, etc are degenerate; '+\
                r"a weight's change doesn't depend on its value. $\alpha$/"+\
                r'$\beta$/$\gamma$/$\delta$ are not meaningful.', \
                (0.03, i-.2), fontsize=6) 
#                r'nonzero weights act the same everywhere. $\alpha$/'+\
#                r"a weight's change is invariant to value. $\alpha$/"+\
        h, = plt.plot( [0], [i], '-o', color=colors_[i], label=sigm_id)
        handles =[h]+handles
        continue
    J=4
    if sigm_id=='x-x^2*':
        plt.annotate(r'($\delta$: $\sigma$(x>$\gamma$)=1', (A[2,i]+0.08, i+0.10), fontsize=6) 
        plt.annotate(r'is not meaningful)', (A[2,i]+0.09, i-0.25), fontsize=6) 
        J=3
    if sigm_id=='xroot':
        plt.annotate(r'$\alpha$/$\delta$: D4 peaks > 0', (A[0.383,i]-0.02, i+0.15), fontsize=6) 
    h, = plt.plot( A[:J,i], [i]*J, 
         '-o', color=colors_[i], label=sigm_id)
    handles =[h]+handles
    if sigm_id=='p=4.37':
        plt.annotate( r'$\alpha$=$\beta$', (A[0,i]-0.04, i+0.25), fontsize=6) 
        plt.annotate( r'$\gamma$', (A[2,i]-0.02, i+0.25), fontsize=6) 
        plt.annotate( r'$\delta$', (A[3,i]-0.02, i+0.25), fontsize=6) 
        continue
    for j in range(J):
#        plt.annotate('abcd'[j], (A[j,i]-0.02, i+0.15), fontsize=6) 
        plt.annotate([r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$'][j], \
                (A[j,i]-0.02, i+0.25), fontsize=6) 
#                (A[j,i]-0.02, i+0.15), fontsize=6) 

plt.yticks(range(l),titles_ordered)

#plt.legend(handles=handles, bbox_to_anchor=(1.,.5), loc='center left') # , mode='expand') 
#plt.tight_layout(rect=[0,0.05,0.85,0.8])
#plt.tight_layout(rect=[0,0.15,0.8,0.8])
plt.tight_layout(rect=[0,0.15,1.0,0.8]) # [left, bot, right, top]
#plt.xticks([0,0.5,1,1.5,2,2.5])
plt.xticks([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5])  # this vs. above line: needs change at tag03939
#plt.xticks([0.25*i for i in range(0,13)])
plt.title(r'Comparison of zone-determining special points of sigmoidal activation functions $\sigma$.'+'\n'+\
        r"Horizontal axis: $v_i=\Sigma_{j}w_{ij}x_{j}$.  Vertical axis: numerical $v_i$ values corresponding to special points of various $\sigma$'s."+'\n'+\
        r'Letting D2($v_i$)=$-(y_i^\star$- $\sigma(v_i))\frac{d}{dt}\sigma(v_i)$ which aligns with $\frac{d^2}{dv_i^2}\sigma(v_i)$ '+\
          r'for some $\sigma$, D4=$\frac{d^2}{dv_i^2}$(D2), subset $v_i$>0, and case $y_i^\star$=0:'+'\n'+\
        r'$\alpha$: max(|D4|).   $\beta$: max(|D2|).   $\gamma$: D4=0 for $v_i$>$\beta$.   $\delta$: local max(|D4|) for $v_i$>$\gamma$.'+'\n'+\
        r'Please see commentary_figures.txt for detailed information.', \
        fontdict={'fontsize':9})

#print(' raw data: '+str(d))
'''
data_as_str = 'raw data: '+', '.join([v+':'+str(k) for v,k in d.items() if v in titles_ordered[:3] ])\
        +',\n'+ ', '.join([v+':'+str(k)+',  ' for v,k in d.items() if v in titles_ordered[3:6] ])\
        +',\n'+ ', '.join([v+':'+str(k)+',  ' for v,k in d.items() if v in titles_ordered[6:9] ])\
        +',\n'+ ', '.join([v+':'+str(k)+',  ' for v,k in d.items() if v in titles_ordered[9: ] ])\
# plt.text(0.95, 0.1, ' raw data: '+data_as_str, va="bottom", ha, fontsize=6)
plt.annotate( data_as_str, (0,0), (0,-20), xycoords='axes fraction', \
        textcoords='offset points', va='top', fontsize=5) # https://stackoverflow.com/questions/7917107/add-footnote-under-the-x-axis-using-matplotlib
'''
 
from numpy import e
def d2(x): return (4**2)*(e**x-e**-x)/(e**x+e**-x)**3
def _tanh(x): return (e**x-e**-x)/(e**x+e**-x)
def _sech(x): return 2/(e**x+e**-x)
def d4(x): 
    x=x*1.000000001
    th,sh=_tanh(x),_sech(x)
    return e**(-2*x**2)*(-3*x+2*(e**(x**2))*(2*x**2-1)*th)
def d2_erf(x):  return 2.5*(e**-(x**2))*_tanh(x)
#    return 4*(th**3)*(sh**2)-8*th*(sh**4)
#    return 4*(e**(2*x))*(4+(e**x)*(-7+e**x))/(e**x+1)**5

color1 = [x/256. for x in [0,90,181]]+[0.6] # colorblind-accessible
color2 = [x/256. for x in [220,50,32]]+[0.6] # https://davidmathlogic.com/colorblind/#%23005AB5-%23DC3220

Range_1 = list(np.linspace(-4.,4.03,100))
#axins = ax.inset_axes([0.80, -0.25, 0.15,0.15]) # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html
axins1 = ax.inset_axes([0.0, -0.4, 0.4,0.3]) # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html
axins1.set_xticks([])
axins1.set_yticks([])
axins1.plot([-4,4], [0,0], '--', color=[0.,0.,0.,0.3])
axins1.plot([-0.004,0.004], [-1.6,1.6], '--', color=[0.,0.,0.,0.3])
axins1.plot(Range_1, [d2_erf(r) for r in Range_1], '-', color=color1)
axins1.plot(Range_1, [d4(r) for r in Range_1], '-', color=color2)
axins1.annotate( r'$v_i$' ,  (0,0), (3.5,-0.4), fontsize=8, color=[0,0,0,0.6]) 

captn_y=-2.7 # 'caption'
captn_x=1.0# when bounds are [0, 2.5].  tag03939
plt.annotate(r'Left: typical shapes of' , (0,0),  (captn_x,captn_y), fontsize=6) #(0.4,-0.25), (1.6,0.3),
#plt.annotate(r'D2($v_i$) (green), D4($v_i$) (red).'  ,  (0,0), (captn_x,captn_y-.5), fontsize=6) #(0.4,-0.25), (1.6,0.3),
plt.annotate(r'D2($v_i$)' ,  (0,0), (captn_x,captn_y-.5), color=color1, fontsize=7) #(0.4,-0.25), (1.6,0.3),
plt.annotate(r'&' ,  (0,0), (captn_x+.125,captn_y-.5), color='black', fontsize=6) #(0.4,-0.25), (1.6,0.3),
plt.annotate(r'D4($v_i$)' ,  (0,0), (captn_x+.15,captn_y-.5), color=color2, fontsize=7) #(0.4,-0.25), (1.6,0.3),
plt.annotate( 'Right: locations of' ,  (0,0), (captn_x,captn_y-1.2), fontsize=6) #(0.4,-0.25), (1.6,0.3),
plt.annotate( 'special points.' ,  (0,0), (captn_x,captn_y-1.7), fontsize=6) #(0.4,-0.25), (1.6,0.3),
plt.annotate( '(Curves are not' ,  (0,0), (captn_x,captn_y-2.5), fontsize=6) #(0.4,-0.25), (1.6,0.3),
plt.annotate( 'vertically to scale)' ,  (0,0), (captn_x,captn_y-3.0), fontsize=6) #(0.4,-0.25), (1.6,0.3),

axins2 = ax.inset_axes([0.6, -0.4, 0.4,0.3]) # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html
axins2.set_xticks([])
axins2.set_yticks([])
Range_2 = list(np.linspace(0,3,100))
axins2.plot([0,0.004], [-1.6,1.1], '--', color=[0.,0.,0.,0.3])
axins2.plot([0,3.3], [0,0], '--', color=[0.,0.,0.,0.3])
#axins2.plot(Range_2, [d2_erf(r) for r in Range_2], '-', color=[0.,1.,0.,0.5])
axins2.plot(Range_2, [d2_erf(r) for r in Range_2], '-', color=color1)
axins2.axvline(0,0,0)
#axins2.plot(Range_2, [d4(r) for r in Range_2], '-', color=[1.,0.,0.,0.37])
axins2.plot(Range_2, [d4(r) for r in Range_2], '-', color=color2)
axins2.annotate( r'$\beta$' ,  (0,0), (.55,.8), fontsize=8) #(0.4,-0.25), (1.6,0.3),
axins2.plot([.625,.626],[-.2,.2],color=[0.,0.,0.,0.3], linewidth=1)
axins2.annotate( r'-$\alpha$' ,  (0,0), (.27,-1.6), fontsize=8) 
axins2.plot([.410,.411],[-.2,.2],color=[0.,0.,0.,0.3], linewidth=1)
axins2.annotate( r'$\gamma$' ,  (0,0), (.9,.35), fontsize=8) 
axins2.plot([.95,.96],[-.2,.2],color=[0.,0.,0.,0.3], linewidth=1)
axins2.plot([.95,.96],[.7,.85],color=[0.,0.,0.,0.3], linewidth=1)
axins2.annotate( r'$\delta$' ,  (0,0), (1.35,.7), fontsize=8) 
axins2.plot([1.4,1.41],[-.2,.2],color=[0.,0.,0.,0.3], linewidth=1)
axins2.annotate( r'$v_i$' ,  (0,0), (3.1,-0.35), fontsize=8, color=[0,0,0,0.6]) 


#ax.indicate_inset_zoom(axins)

plt.show()
plt.close()
