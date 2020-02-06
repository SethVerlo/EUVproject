import ChiantiPy.core as ch
import numpy as np
import ChiantiPy.tools.filters as chfilters
import matplotlib.pyplot as plt

t = 10.**(3.84 + 0.05*np.arange(8.))
H1 = ch.ion('h_1', temperature=t, eDensity=1.e+14, em=1.e+27)
H1.popPlot()
H1.intensityPlot(wvlRange=[6564,6565],linLog='log', index=4)
H1.intensityList(wvlRange=[4000,7000], index=4)
plt.show(H1)

H1a = ch.ioneq(1)
H1a.load()
H1a.plot()
#plt.xlim(0,3e4)
plt.tight_layout()
plt.show(H1a)                 
