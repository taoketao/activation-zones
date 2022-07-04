 
import matplotlib.pyplot as plt
plt.text( 0.01,0,
        "'p=2' refers to the sigmoidal curve f(x)=x/(1+x^2)^(1/2). General pattern: x/(1+|x|^p)^(1/p) \n"+\
        "Gudder(mann): arctan(tanh(x))*4/pi.\n exp*: {x>0: 1-e^-x.  x<=0: e^x-1.} \n"+\
        "'p=1' and 'exp*' are the only plotted curves whose points are all equally spaced.\n"+\
        "Alternative versions of tanh, such as -1+2/(1+2^-x) or -1+2/(1+10^-x), retain the ratios of special points' values. \n"+\
        "In exp*, if you replaced 'e' with '2', you'd get (0,1,2,3) as your sequence. With '4', you'd get the same profile as p=1.\n"+\
        "...That is to say: special point 'spectra' do not correspond to unique sigmoid functions.' \n"+\
        "An erratum: meant to say, 'Define D4 := d^2/dw^2 D2.' \n"+\
        "An erratum: delete the words 'from drift' at the end of the line starting with 'beta'. \n"+\
        "An erratum: meant to say, 'delta: a distal local peak/trough of D4...' \n"+\
        '')
#plt.tight_layout(rect=[0,0.01,1,0.02])
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

plt.show()
plt.close()
